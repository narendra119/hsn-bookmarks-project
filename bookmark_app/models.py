from django.db import models
from django.utils import timezone


# Create your models here.

class Customer(models.Model):
  name = models.CharField(max_length = 200, null = True)
  latitude = models.DecimalField(max_digits = 9, decimal_places = 6, null = True)
  longitude = models.DecimalField(max_digits = 9, decimal_places = 6, null = True)
  

  class Meta:
      db_table = 'customer_table'
      ordering = ['name']

  def __str__(self):
    return self.name

class BookMark(models.Model):
  title = models.CharField(max_length = 255)
  url = models.URLField()
  source_name = models.CharField(help_text='Publication Name',max_length = 255)
  date_added = models.DateTimeField(default = timezone.now)
  customer_name = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'bookmarks', null = False)


  class Meta:
      db_table = 'bookmark_table'
      ordering = ['title']

  def __str__(self):
    return self.title
    
  
