from django.urls import path
from . import views

urlpatterns = [
path("",views.index,name="index"),
path("bigshaq/",views.bigshaq,name="big shaq"),
]
