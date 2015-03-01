from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from grocery.models import *

# Create your views here.
def index(request):
    context = {
        'lists': [str(i) for i in List.objects.all()]
    }
    return render(request, 'grocery/index.html', context)
