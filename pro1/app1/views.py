from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView, DetailView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class EmployeeListView(ListView):
    context_object_name = 'employee'
    model = models.Employee


class EmployeeDetailView(DetailView):
    context_object_name = 'employee_details'
    model = models.Employee
    template_name = 'app1/detail.html'
