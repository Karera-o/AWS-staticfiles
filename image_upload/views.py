# image_upload/views.py

from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()

    images = UploadedImage.objects.all()
    return render(request, 'image_upload/image_upload.html', {'form': form, 'images': images})


# image_upload/views.py

# from django.shortcuts import render,redirect
# from .models import UploadedImage

# def image_upload(request):
#     if request.method == 'POST':
#         form = UploadedImage(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('image_upload')  # Redirect back to the upload page
#     else:
#         form = UploadedImage()

#     images = UploadedImage.objects.all()
#     return render(request, 'image_upload/image_upload.html', {'form': form, 'images': images})

def image_list(request):
    images = UploadedImage.objects.all()
    return render(request, 'image_upload/image_list.html', {'images': images})
