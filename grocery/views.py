from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt    # Because it's a pain to do this with mobile
import json
import copy

from grocery.models import *

# Create your views here.
def index(request):
    context = {
        'lists': [i for i in List.objects.all()]
    }
    return render(request, 'grocery/index.html', context)
    
# API
API_RETURN_DATA_FORMAT = {
    'data': [],
    'len': 0,
    'status': 'OK',
    'status_message': 'OK',
}

@csrf_exempt
def list_item(request, list_item_id = -1, action = ''):
    return_data = copy.deepcopy(API_RETURN_DATA_FORMAT)
    
    if request.method == 'GET':
        if action == 'toggle': 
            li = List_Item.objects.get(id = int(list_item_id))
            li.bought = not li.bought
            li.save()
            
            return HttpResponse(json.dumps(return_data), content_type="application/json")
        else:
            return_data['status'] = 'ERROR'
            return_data['status_message'] = 'Request action not supported'
            return HttpResponse(json.dumps(return_data))
    elif request.method == 'POST':
        d = json.loads(request.body)
        i = Item(desc=d['name'])
        i.save()
        
        li = List_Item(item=i, list=List.objects.get(id=int(d['l_id'])))
        li.save()
        #l = List(title = 
        return HttpResponse(json.dumps(return_data))
    else:
        return_data['status'] = 'ERROR'
        return_data['status_message'] = 'Request method not supported'
        return HttpResponse(json.dumps(return_data))

@csrf_exempt
def list(request, list_id = None):
    return_data = copy.deepcopy(API_RETURN_DATA_FORMAT)
    
    if request.method == 'GET':
        if not list_id: # Get a list of all the lists
            for i in List.objects.all():
                return_data['data'].append({
                    'id': i.id,
                    'title': i.title,
                    'status': i.status
                })
            return_data['len'] = len(return_data['data'])
            
            return HttpResponse(json.dumps(return_data), content_type="application/json")
        elif list_id:
            for i in List_Item.objects.filter(list_id = int(list_id)):
                return_data['data'].append({
                    'id': i.id,
                    'l_id': int(list_id),
                    'desc': i.item.desc,
                    'bought': i.bought,
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
