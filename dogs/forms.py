from django import forms

from dogs.models import Dog

class DogForms(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'