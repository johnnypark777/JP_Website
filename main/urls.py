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
    path('imagesystem/', file_list, name='file_list'),
    path('imagesystem/upload/', upload_file, name='upload_file'),
    path('imagesystem/<int:pk>/', delete_file, name='delete_file'),
    path('api/image_delete/<int:pk>', image_delete, name='image'),
    path('api/imagelist/', image_list, name='image_list'),
    path('api/image_upload/', image_upload, name='image_upload'),
    path('api/image/<int:pk>', image, name='image'),
    path('api/food_upload', food_upload, name='food_upload'),
    path('api/foodlist/', food_list, name='food_list'),
    path('api/food_delete/<int:pk>', food_delete, name='delete_food'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
