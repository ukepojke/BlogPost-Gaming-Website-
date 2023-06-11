from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('post/<int:id>',post_detail),
    path('category/',post_category),
    path('category/<int:id>',detail_category),
    path('post/create/',post_create),
]