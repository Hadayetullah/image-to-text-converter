from django.db import models

# Create your models here.


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    ocr_result = models.TextField(blank=True)
