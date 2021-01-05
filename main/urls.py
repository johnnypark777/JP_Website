from django.urls import path
from .views import *

# Importing image
from django.conf.urls.static import static
from JP_Website import settings

urlpatterns = [
    path('projects/', projects_view, name='projects'),
    path('bigshaq1/', bigshaq),
    path('poachedegg/', poachedegg),
    path('', index),
    path('1999/', home_view),
    path('benson/',benson),
    path('imagesystem/', book_list, name='book_list'),
    path('imagesystem/upload/', upload_book, name='upload_book'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
