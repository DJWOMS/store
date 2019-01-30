from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from .models import Profile
from .forms import ProfileForm


class ProfileDetail(LoginRequiredMixin, DetailView):
    """Вывод профиля пользователя"""
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    """Редактирование профиля"""
    form_class = ProfileForm
    model = Profile
    template_name = "profiles/profile_update.html"

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.instance.country)
        print(form.instance.state)
        print(form.instance.city)
        return super().form_invalid(form)
