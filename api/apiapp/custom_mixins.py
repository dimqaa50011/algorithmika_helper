from .serializers import TgUserSerializer, MiniCourseSerializer, StudentSerializer
from .models import TgUser, MiniCours, Student


class TgUserAPIMixin:
    serializer_class = TgUserSerializer
    queryset = TgUser.objects.all()


class MiniCourseMixin:
    serializer_class = MiniCourseSerializer
    queryset = MiniCours.objects.all()


class StudentMixin:
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    