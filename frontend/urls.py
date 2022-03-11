from operator import index
from django.urls import path
from . import views
from . import app

urlpatterns = [
    path('predict', app.predict, name='predict'),
    path('', views.main, name='home')

]