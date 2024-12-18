from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from books.models import *

class customerlist(View):
    def get(self,request):
        data = {"customerviewlist":customer_model.objects.all()}

        return render(request,"customer_list.html",data)

    
class aboutpage(View):
    def get(self,request):
        return render(request,"aboutpage.html")
    
class booklist(View):
    def get(self,request):
        data = {"listofbook":book_models.objects.all()}
        print(data,"summa")
        return render(request,'landingpage.html',data)
    
# class landingpage(View):
#     def get(self,request):
#         return render(request,'landingpage.html')
    
class addcustomer(View):
    def get(self,request):
        data = {'addcustomer':customer_form}
        return render(request,'addcustomer.html',data)
    def post(self,request):
        new_customer = customer_form(request.POST)
        if new_customer.is_valid():
            new_customer.save()
            return redirect('/customerlist/')
        else:
            print(new_customer.errors)

class updatecustomer(View):
    def get(self,request,id):
        selected_customer = customer_model.objects.get(id = id)
        data = {'addcustomer':customer_form(instance = selected_customer)}
        return render(request,'addcustomer.html',data)
    def post(self,request,pk):
        selected_customer = customer_model.objects.get(id = id)
        new_customer = customer_form(request.POST,instance=selected_customer)
        if new_customer.is_valid():
            new_customer.save()
            return redirect('/customerlist/')
        else:
            print(new_customer.errors)


class deletecustomer(View):
    def get(self,request,id):
        data = customer_model.objects.get(id = id)
        data.delete()
        return redirect('/customerlist/')