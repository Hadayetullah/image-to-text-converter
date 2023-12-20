
from django.urls import path
from .views import upload_image, image_detail
app_name = 'app_ocr'


urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('image/<int:pk>/', image_detail, name='image_detail'),
]
