from django.shortcuts import render
# from templates import index
from django.views.generic import TemplateView
from django.urls import reverse


# Create your views here.
def index(request):
	return render(request, 'zeichentrickfilm/index.html')