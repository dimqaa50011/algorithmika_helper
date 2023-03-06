from django.urls import path

from .apps import ApiappConfig
from . import views as api_views

app_name = ApiappConfig.name

urlpatterns = [
    path('user/', api_views.CreateTgUser.as_view()),
    path('user/<int:tg_id>/', api_views.ReadOrUpdateTgUser.as_view()),
    path('user/list/', api_views.ListTgUser.as_view()),
]