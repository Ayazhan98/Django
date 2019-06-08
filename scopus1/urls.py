from django.urls import path
from .views import *

urlpatterns = [

    path('', paper ,name='paper'),
]