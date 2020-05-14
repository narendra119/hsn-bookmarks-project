from django.contrib import admin
from django.urls import path, include
from bookmark_app import views, api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('bookmarks/', include('bookmark_app.urls')),
    path('api/create', api.create_bookmark.as_view(), name= 'create-book')
    

]