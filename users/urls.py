from django.urls import path
from users.apps import UsersConfig
from users.forms import UserRegisterForm

from users.views import UserRegisterView, UserUpdateView, \
    user_generate_new_password_view, UserLoginView, UserProfileView, UserUpdateView, UserPasswordChangeView, \
    UserLogoutView, UsersListView

app_name = UsersConfig.name

urlpatterns = [
    # работа с аккаунтом
    path('', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('update/', UserUpdateView.as_view(),name='user_update'),
    path('change_password/', UserPasswordChangeView.as_view(), name='user_change_password'),
    path('profile/genpassword/', user_generate_new_password_view, name='user_generate_new_password'),
    # просмотр других пользователей
    path('all_users/', UsersListView.as_view(), name='users_list_view'),
]
