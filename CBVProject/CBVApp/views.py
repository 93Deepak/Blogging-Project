from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.

class Hello(TemplateView):
    template_name='CBVApp/hello.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['id']=101
        context['name']='Ramu'
        context['salary']=12000.00
        return context
