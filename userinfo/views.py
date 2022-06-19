from django.views.generic import UpdateView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm
from .models import UserInfo


class UserInfoUpdateView(UpdateView):
    model = UserInfo
    template_name = 'userinfo/userinfo_form.html'
    fields = ['first_name', 'last_name', 'phone', 'address']
    success_url = '/userinfo/profile/'


user_info_update_view = UserInfoUpdateView.as_view()


class UserInfoView(TemplateView):
    template_name = 'userinfo/userinfo_detail.html'


user_info_view = UserInfoView.as_view()


def register(request):
    if request.user.is_authenticated:
        return redirect('userinfo:profile')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)

            profile = UserInfo.objects.create(user=user)

            login(request, user) # biz yaratgan userni login qiladi
            messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz!')
            return redirect('userinfo:update_profile', pk=profile.pk)

    return render(request, 'userinfo/register.html', {'form': SignUpForm()})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('userinfo:profile')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz!')
                return redirect("userinfo:profile")
    return render(request, 'userinfo/login.html', {'form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    messages.success(request, 'Tizimdan chiqdingiz!')
    return redirect('main:home')

