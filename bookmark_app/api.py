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

import json

class create_bookmark(View):
  def  post(self, request):
    data = request.body.decode('utf8')
    data = json.loads(data)
    try: 
      # customer_name  = Customer.objects.get(name = data['customer_name'])
      # new_bookmark = BookMark(data)
      # new_bookmark.customer_name = customer_name
      # new_bookmark.save()
      return JsonResponse({'created':data}, safe = False)
    except:
      return JsonResponse({'error':'not a valid data'})
