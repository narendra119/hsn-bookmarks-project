from django.contrib import admin
from django.urls import path, include
from bookmark_app import views, api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('api/create', api.create_bookmark.as_view(), name= 'create-book'),
    path('api/browse', api.browse_bookmarks.as_view(), name='browse-bookmarks'),

    path('api/bookmarks', api.show_bookmarks, name='bookmarks'),
    path('api/bookmarks/delete/<int:id>', api.del_bookmarks, name = "del-marks"),

]
