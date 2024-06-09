import string
import secrets
import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


# Create your views here.

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):

        user = form.save()
        user.is_active = False
        token = secrets.token_hex(32)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/register/confirm/{token}'
        send_mail(
            subject='Подтверждение регистрации.',
            message=f'Для подтверждения регистрации перейдите по ссылке {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_confirm(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True

    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    if request.method == 'POST':
        print(request)
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        characters = string.ascii_letters + string.digits  # + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        send_mail(
            subject='Восстановление пароля.',
            message=f'Для учетной записи {email} был установлен новый пароль: {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )
        user.set_password(password)
        user.save()
        return redirect(reverse('users:reset-password-success'))

    return render(request, 'users/reset-password.html')


def reset_password_success(request):
    return render(request, 'users/reset-password-success.html')
