import datetime

from django import forms

from dogs.models import Dog, DogParent

from users.forms import StyleFormMixin


class DogForms(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('owner', 'is_active', 'views',)

    def clean_birth_date(self):
        cleaned_data = self.cleaned_data['birth_date']
        now_year = datetime.datetime.now().year
        if now_year - cleaned_data.year > 35:
            raise forms.ValidationError('Собака должна быть моложе 35 лет')
        return cleaned_data


class DogAdminForm(DogForms):
    class Meta:
        model = Dog
        exclude = ('is_active',)


class DogParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = DogParent
        fields = '__all__'
