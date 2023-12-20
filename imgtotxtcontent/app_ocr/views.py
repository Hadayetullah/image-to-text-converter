from django.shortcuts import render, redirect
from .forms import ImageUploadForm
import pytesseract
from PIL import Image
from .models import UploadedImage
# Create your views here.


def upload_image(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save()

            # Perform OCR using Tesseract
            img = Image.open(form_obj.image.path)
            text = pytesseract.image_to_string(img)

            # Save OCR result to the model
            form_obj.ocr_result = text
            form_obj.save()

            return redirect('app_ocr:image_detail', pk=form_obj.pk)

    else:
        form = ImageUploadForm()

    return render(request, 'app_ocr/upload_image.html', {'form': form})


def image_detail(request, pk):
    image = UploadedImage.objects.get(pk=pk)
    return render(request, 'app_ocr/image_detail.html', {'image': image})
