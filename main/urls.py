from django.urls import path
from .views import *

# Importing image
from django.conf.urls.static import static
from JP_Website import settings

urlpatterns = [
    path('projects/', projects_view, name='projects'),
    path('bigshaq1/', bigshaq),
    path('poachedegg/', poachedegg),
    path('',index),
    path('1999/',home_view),
]
