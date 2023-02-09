import tornado
import tornadoredis
from tornadio2 import SocketConnection
from tornadio2.conn import event
import django
from importlib import import_module
from django.conf import settings
import json

from settings import REDIS_PASSWORD, REDIS_PORT, REDIS_HOST

_engine = import_module(settings.SESSION_ENGINE)


def get_session(session_key):
    return _engine.SessionStore(session_key)


def get_user(session):
    class Dummy(object):
        pass

    django_request = Dummy()
    django_request.session = session

    return django.contrib.auth.get_user(django_request)


unjson = json.loads
json = json.dumps


class Connection(SocketConnection):
    def __init(self, *args, **kwargs):
        super(Connection, self).__init__(*args, **kwargs)
        self.listen_redis()

    @tornado.gen.engine
    def listen_redis(self):
        self.redis_client = tornadoredis.Client(
            host=REDIS_HOST,
            port=REDIS_PORT,
            password=REDIS_PASSWORD
        )
        self.redis_client.connect()

        yield tornado.gen.Task(self.redis_client.subscribe, [
            'order_lock',
            'order_done'
        ])
        self.redis_client.listen(self.on_redis_queue)

    def on_open(self, info):
        self.django_session = get_session(info.get_cookie('sessionid').value)


    def login(self):
        self.user = get_user(self.django_session)
        self.is_client = self.user.has_perm('order.lock')
        self.is_moder = self.user.has_perm('order.delete')

    def on_message(self, message):
        pass

    def on_redis_queue(self, message):
        if message.kind == 'message':
            message_body = unjson(message.body)

            if message.channel == 'order_lock':
                self.on_lock(message_body)

            if message.channel == 'order_done':
                self.on_done(message_body)

    def on_lock(self, message):
        if message['user'] != self.user.pk:
            self.emit('lock', message)

    def on_done(self, message):
        if message['user'] != self.user.pk:
            if self.is_client:
                message['action'] = 'hide'
            else:
                message['action'] = 'highlight'

            self.emit('done', message)

    def on_close(self):
        self.redis_client.unsubscribe([
            'order_lock',
            'order_done'
        ])
        self.redis_client.disconnect()


