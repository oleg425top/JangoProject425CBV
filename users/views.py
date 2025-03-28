from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from users.forms import UserRegisterForms


def user_register_view(request):
    if request.metod == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            new_user = form.save()
            print(new_user)
            print(form.cleaned_data['password'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('dogs/index'))
        context = {
            'title':'Создать акаунт',
            'forms': UserRegisterForms
        }
        return render(request, 'users/user_register.html', context=context)