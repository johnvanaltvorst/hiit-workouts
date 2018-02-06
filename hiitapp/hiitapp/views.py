from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    context = 'Welcome home'
    return render(request,'base.html',{'context':context})

class HomePageView(TemplateView):
    template_name = 'base.html'
