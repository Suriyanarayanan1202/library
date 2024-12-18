from django.urls import path
from .views import *
from books.views import *

urlpatterns = [
    path('customerlist/',customerlist.as_view()),
    path('about/',aboutpage.as_view()),
    path('',booklist.as_view()),
    path('addcustomer/',addcustomer.as_view()),
    path('delcustomer/<int:id>/',deletecustomer.as_view(),name='deletecust'),
    path('updatecustomer/<int:id>/',updatecustomer.as_view(),name='update_customer'),
    path('deletebook/<int:id>/',deletebook.as_view(),name='delete_book'),
    path('updatebook/<int:id>/',updatebook.as_view(),name='update_book'),
    path('transcationlist/',transcation_list.as_view()),

]