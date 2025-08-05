from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import UserRegisterForm, UserProfileEditForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        messages.success(
            self.request, "Вы успешно зарегистрировались. Пожалуйста, войдите."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ошибка регистрации. Проверьте введенные данные.")
        return super().form_invalid(form)

class UserLoginView(LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy(
        "mailing:home"
    )

    def get_success_url(self):
        return self.success_url


class UserLogoutView(LogoutView):
    next_page = reverse_lazy(
        "users:login"
    )


@login_required
def profile(request):
    return render(request, "users/profile.html")


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = UserProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен.")
            return redirect("users:profile")
        else:
            messages.error(
                request, "Ошибка обновления профиля. Проверьте введенные данные."
            )
    else:
        form = UserProfileEditForm(instance=request.user)
    return render(request, "users/profile_edit.html")