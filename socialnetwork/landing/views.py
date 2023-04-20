from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing/index.html')