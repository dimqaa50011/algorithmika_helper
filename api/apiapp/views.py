from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView

from .custom_mixins import TgUserAPIMixin, MiniCourseMixin, StudentMixin
from .serializers import StudentSerializer
from .models import Student


class CreateTgUser(TgUserAPIMixin, CreateAPIView):
    pass


class ListTgUser(TgUserAPIMixin, ListAPIView):
    pass


class ReadOrUpdateTgUser(TgUserAPIMixin, RetrieveUpdateAPIView):
    lookup_field = 'tg_id'


class ListMiniCousres(MiniCourseMixin, ListAPIView):
    pass


class ListStudents(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(course_id=self.kwargs.get('pk'), is_presence=False)


class ReadOrUpdateStudent(StudentMixin, RetrieveUpdateAPIView):
    pass
