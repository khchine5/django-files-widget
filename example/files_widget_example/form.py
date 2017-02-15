from django.forms import ModelForm

from models import MyModelFile_Widget


class MyModelForm(ModelForm):
    class Meta:
        model = MyModelFile_Widget
        fields = ('name', 'image', 'images')
