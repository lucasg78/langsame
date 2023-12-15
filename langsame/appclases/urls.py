from django.urls import path
from appclases.views import *

urlpatterns = [
    path("", inicio),
    path("clases/", clases),
]
