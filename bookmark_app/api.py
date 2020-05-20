from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views.decorators.http import require_POST

from .models import Customer, BookMark
from django.contrib.auth import (
  authenticate,
  get_user_model,
  login,
  logout,
  )

import json
from .forms import CreateBookMarkForm
from .serializers import BookMarkSerializer
from rest_framework.views import APIView


# List the Bookmarks
# /api/bookmarks
def show_bookmarks(request):
  """
      API EndPoint to list the BookMark Objects
  """
  bookmarks = BookMark.objects.all()
  ser_obj = serializers.serialize('json', bookmarks)
  return JsonResponse(ser_obj, safe = False)


# Delete the Bookmark with the id(captured from the url)
# /api/bookmarks/delete
def del_bookmarks(request, id):
  """
      API EndPoint to delete the BookMark Object
  """
  bookmark = BookMark.objects.get(id=id)
  bookmark.delete()
  return redirect(reverse('bookmarks'))


# Api endpoint to create BookMark model
# api/create
@method_decorator(csrf_exempt, name = 'dispatch')
class create_bookmark(APIView):
  """ API EndPoint to create BookMark Objects. Input data to be passed as a Json Object via request body  which can be accessed by request.data
  """
  def post(self, request):
      data = request.data
      
      title = data['title']
      source_name = data['source_name']
      url = data['url']
      customer_name_id = data['customer_name_id']

      try:
        bookmark = BookMark(title=title, source_name=source_name, url=url, customer_name_id=customer_name_id)
        bookmark.save()
      except:
        return JsonResponse({'error':'object not created'})
      return JsonResponse({'created':'ok'})



# /api/browse
@method_decorator(csrf_exempt, name = 'dispatch')
class browse_bookmarks(APIView):
    """ API EndPoint To Browse the BookMark objects filter by Query Parameters passed via URL.    
    """    
    def get(self, request):
        latitude = self.request.query_params.get('lat')
        longitude = self.request.query_params.get('long')
        
        if latitude and longitude:
          queryset = BookMark.objects.filter(customer_name__latitude = latitude, customer_name__longitude = longitude)
        
        start_date = self.request.query_params.get('start_date').strftime("%m/%d/%Y")
        end_date = self.request.query_params.get('end_date').strftime("%m/%d/%Y")
        
        if start_date and end_date:
          queryset = BookMark.objects.filter(date_added__range = [start_date, end_date])

        title_string = request.query_params.get('title_contains') 
        if title_string:
          queryset.filter(title__contains=title_string)
          
        source_name = request.query_params.get('source_name')
        if source_name:
          queryset.filter(source_name=source_name)
        
        customer_name_id = request.query_params.get('customer_id')
        if customer_name_id:
          queryset.filter(customer_name_id = customer_name_id)

        serializer = BookMarkSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)




  