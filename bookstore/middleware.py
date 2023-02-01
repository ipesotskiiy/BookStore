from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs

User = get_user_model()


@database_sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope):
        parsed_query_string = parse_qs(scope['query_string'])
        get_token = parsed_query_string.get(b'token')[0].decode('utf-8')

        try:
            token = AccessToken(get_token)
            scope['user'] = await get_user(token['user_id'])

        except (InvalidToken, TokenError) as e:
            print(e)
            scope['user'] = AnonymousUser()

        return await self.app(scope)
