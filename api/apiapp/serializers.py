from rest_framework.serializers import ModelSerializer

from .models import TgUser, MiniCours, Student


class TgUserSerializer(ModelSerializer):
    class Meta:
        model = TgUser
        fields = '__all__'


class MiniCourseSerializer(ModelSerializer):
    class Meta:
        model = MiniCours
        fields = '__all__'


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
