from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json

from grocery.models import *

# Create your views here.
def index(request):
    context = {
        'lists': [i for i in List.objects.all()]
    }
    return render(request, 'grocery/index.html', context)
    
# API
def list(request):
    response_data = []
    for i in List.objects.all():
        response_data.append({
            'id': i.id,
            'title': i.title,
            'status': i.status
        })
    
    return HttpResponse(json.dumps({
        'data': response_data
    }), content_type="application/json")
