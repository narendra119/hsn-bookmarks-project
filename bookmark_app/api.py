from django.shortcuts import render, redirect
from django.http import JsonResponse

from django.views import View

from .models import Customer, BookMark
from django.contrib.auth import (
  authenticate,
  get_user_model,
  login,
  logout,
  )

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_bookmark(request):
  if request.method == 'POST':
    data = request.POST
    title = data['title']
    customer_name_id = data['customer_name_id']
    url = data['url'] 
    source_name = data['source_name']
    
    # return JsonResponse({'data':data})
    try:
      new_bookmark = BookMark(title = title, customer_name_id = customer_name_id, 
                              url = url, source_name = source_name)
      new_bookmark.save()
      return JsonResponse({'created':data}, safe = False)
    except:
      return JsonResponse({'error':'data not valid'})

    
    return JsonResponse(request.POST)


"""
class create(View):
  def  post(self, request):
    data = request.body.decode('utf8')
    data = json.loads(data)
    return JsonResponse({'created':data})
    try: 
      # customer_name  = Customer.objects.get(name = data['customer_name'])
      # new_bookmark = BookMark(data)
      # new_bookmark.customer_name = customer_name
      # new_bookmark.save()
      return JsonResponse({'created':data}, safe = False)
    except:
      return JsonResponse({'error':'not a valid data'})
"""