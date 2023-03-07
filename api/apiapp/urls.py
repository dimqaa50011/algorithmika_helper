from django.urls import path

from .apps import ApiappConfig
from . import views as api_views

app_name = ApiappConfig.name

urlpatterns = [
    path('user/', api_views.CreateTgUser.as_view()),
    path('user/<int:tg_id>/', api_views.ReadOrUpdateTgUser.as_view()),
    path('user/list/', api_views.ListTgUser.as_view()),
    path('course/list/', api_views.ListMiniCousres.as_view()),
    path('course/<int:pk>/', api_views.ReadOrUpdateMiniCourse.as_view()),
    path('student/list/<int:pk>', api_views.ListStudents.as_view()),
    path('student/report/<int:pk>', api_views.ListStudentsForReport.as_view()),
    path('student/<int:pk>', api_views.ReadOrUpdateStudent.as_view()),
]