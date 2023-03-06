from rest_framework.serializers import ModelSerializer

from .models import TgUser


class TgUserSerializer(ModelSerializer):
    class Meta:
        model = TgUser
        fields = '__all__'
