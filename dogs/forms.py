from django import forms

from dogs.models import Dog

from users.forms import StyleFormMixin

class DogForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'