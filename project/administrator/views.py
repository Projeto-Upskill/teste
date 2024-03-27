from django.shortcuts import render
from django.views.generic import CreateView


class AdminCreateView(CreateView):
    template_name = 'admin_register.html'
