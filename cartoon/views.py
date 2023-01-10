# Create your views here.
from django.shortcuts import render
from .forms import ImageUploadForm
from PIL import Image



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Open the image file and convert it to grayscale
            image = Image.open(request.FILES['image'])
            image = image.convert('L')

            # Save the grayscale version of the image
            image.save('static/grayscale.jpg')

            # Convert into the cartoon version of the image
            image = image.point(lambda x: 255 if x > 128 else 0, '1')
            image.save('static/cartoon.jpg')

            return render(request, 'upload_image.html', {'form': form,
                                                         'cartoon_image': 'static/cartoon.jpg',
                                                         'img_obj': 'static/grayscale.jpg'}
                          )
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})
