from django.urls import path
from form_app.views import *

urlpatterns = [
    path('',home_view,name='home_view'),
    path('bloglist/', blog_list_view,name='blog_list_view'),
    path('blogadd/',blog_add_view,name='blog_add_view'),
]