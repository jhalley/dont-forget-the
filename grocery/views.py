from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt    # Because it's a pain to do this with mobile
import json

from grocery.models import *

# Create your views here.
def index(request):
    context = {
        'lists': [i for i in List.objects.all()]
    }
    return render(request, 'grocery/index.html', context)
    
# API
@csrf_exempt
def list(request):
    return_data = {
        'data': [],
        'len': 0,
        'status': 'OK',
        'status_message': 'OK',
    }
    
    if request.method == 'GET':
        for i in List.objects.all():
            return_data['data'].append({
                'id': i.id,
                'title': i.title,
                'status': i.status
            })
        return_data['len'] = len(return_data['data'])
        
        return HttpResponse(json.dumps(return_data), content_type="application/json")
    elif request.method == 'POST':
        l = List(title=json.loads(request.body)['name'], status=List.OPEN)
        l.save()
        #l = List(title = 
        return HttpResponse(json.dumps(return_data))
    else:
        return_data['status'] = 'ERROR'
        return_data['status_message'] = 'Request method not supported'
        return HttpResponse(json.dumps(return_data))
