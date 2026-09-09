from django.urls import path, include

from newapp import views
from newapp.apps import NewappConfig

app_name = NewappConfig.name

urlpatterns = [
    path('', views.home, name='home'),
]
