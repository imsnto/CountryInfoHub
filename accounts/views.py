from django.shortcuts import render

from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


