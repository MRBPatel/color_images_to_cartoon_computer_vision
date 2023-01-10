from django import forms
from .models import Image


class ImageUploadForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ('image',)
