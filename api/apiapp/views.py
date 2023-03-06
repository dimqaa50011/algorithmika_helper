from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView

from .custom_mixins import TgUserAPIMixin


class CreateTgUser(TgUserAPIMixin, CreateAPIView):
    pass


class ListTgUser(TgUserAPIMixin, ListAPIView):
    pass


class ReadOrUpdateTgUser(TgUserAPIMixin, RetrieveUpdateAPIView):
    lookup_field = 'tg_id'
