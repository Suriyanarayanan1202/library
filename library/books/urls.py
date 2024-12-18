from django.urls import path
from .views import *


urlpatterns = [
    path('booklist/',booklist.as_view()),
    path('addbooks/',addbook.as_view()),
    path('issuethis/<int:id>/',issuebook.as_view(),name='issue'),
    path('returnbook/<int:id>/',returnbook.as_view(),name="returnbooknow"),
   ]