from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import aauthenticate, authenticate, login

from users.forms import UserRegisterForms, UserLoginForm


def user_register_view(request):
    if request.method == 'POST':
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

def user_login_view(request):
    if __name__ == '__main__':
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                user = authenticate(email=cleaned_data['email'], password=cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect(reverse('dogs:index'))
                return HttpResponseRedirect('dfgdfgdfgd')
    context = {
        'title': 'Вход',
        'form': UserLoginForm
    }
    return render(request, 'users')