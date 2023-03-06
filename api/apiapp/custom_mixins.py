from .serializers import TgUserSerializer
from .models import TgUser


class TgUserAPIMixin:
    serializer_class = TgUserSerializer
    queryset = TgUser.objects.all()
    