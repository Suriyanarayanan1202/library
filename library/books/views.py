from django.shortcuts import render,redirect
from .models import *
from django.views import View
from .forms import *
from django.contrib import messages


class booklist(View):
    def get(self,request):
        data = {"listofbook":book_models.objects.all()}
        return render(request,'landingpage.html',data)
    
class addbook(View):
    def get(self,request):
        data = {'addbooks':book_forms}
        return render(request,'addbooks.html',data)
    def post(self,request):
        new_books = book_forms(request.POST)
        if new_books.is_valid():
            new_books.save()
            messages.success(request,f"{new_books} is add successfully")
            return redirect('/books/booklist/')
        else:
            print(new_books.error)

class updatebook(View):
    def get(self,request,id):
        selected_book = book_models.objects.get(id = id)
        data = {'addbooks':book_forms(instance=selected_book)}
        return render(request,'addbooks.html',data)
    def post(self,request,id):
        selected_book = book_models.objects.get(id = id)
        updated_book = book_forms(request.POST,instance=selected_book)
        if updated_book.is_valid():
            updated_book.save()
            messages.success(request,f"{updated_book} is updated successfully")
            return redirect('/books/booklist/')
        else:
            print(updated_book.error)

            
class deletebook(View):
    def get(self,request,id):
        selected_book = book_models.objects.get(id = id)
        selected_book.delete()
        messages.success(request,f"{selected_book.title} is Deleted successfully")
        return redirect('/books/booklist/')

class transcation_list(View):
    def get(self,request):
        data = {"listoftranscation":transaction_model.objects.all()}
        return render(request,"transactionpage.html",data)
    

from .models import *
from customer.models import *
from decimal import Decimal

class issuebook(View):
    def get(self,request,id):
        selected_book = book_models.objects.get(id = id)
        selected_customer = customer_model.objects.all()
        return render(request,'issuebook.html',{"readbook":selected_book,"member":selected_customer})
    
    def post(self,request,id):

        book = book_models.objects.get(id = id)
        member = customer_model.objects.get(id = request.POST['member_id'])

        if member.outstanding_amount > 500:
            messages.error(request,"Your Outstanding Amount is Too Much , Clear The Outstandig Amount ")
            return redirect('/')
        
        if book.avaiable:
            book.avaiable = False
            book.save()

            transaction_model.objects.create(book = book,customer = member,issue_date = timezone.now())
            messages.success(request,f"{book.title} is Issued to {member.fullname}")
            return redirect('/')
        else:
            messages.error(request,"Book is Not Avaiable")
            return redirect('/')
        
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.utils import timezone
from django.contrib import messages
from decimal import Decimal
from datetime import datetime
from .models import *

class returnbook(View):
    GRACE_PERIOD_DAYS = 14
    RENTAL_FEE_PER_DAY = Decimal('50.00')

    def get(self, request, id):
        transaction = transaction_model.objects.get(id =id)

        context = {
            'book': transaction.book,
            'member': transaction.customer,
        }
        return render(request, 'returnpage.html', context)
    
    def post(self, request, transaction_id):
        transaction = get_object_or_404(transaction_model, id=transaction_id)
        return_date_str = request.POST.get('return_date')

        if not return_date_str:
            messages.error(request, 'Return date is required.')
            return redirect('/')

        try:
            # Parse and make return date timezone-aware
            return_date = timezone.make_aware(
                datetime.strptime(return_date_str, '%Y-%m-%dT%H:%M'),
                timezone.get_current_timezone()
            )

            # Ensure issue_date is timezone-aware
            borrow_date = transaction.issue_date
            if timezone.is_naive(borrow_date):
                borrow_date = timezone.make_aware(borrow_date, timezone.get_current_timezone())

            # Calculate days borrowed and rental fee
            days_borrowed = (return_date - borrow_date).days
            rental_fee = Decimal(max(0, days_borrowed - self.GRACE_PERIOD_DAYS)) * self.RENTAL_FEE_PER_DAY

            # Update book availability, member debt, and transaction details
            transaction.book.available = True
            transaction.book.save()

            transaction.member.outstanding_debt += rental_fee
            transaction.member.save()

            transaction.return_date = return_date
            transaction.fee = rental_fee
            transaction.save()

            # Success message and redirection
            messages.success(request, f'Book "{transaction.book.title}" returned successfully. Rental fee: ₹{rental_fee}')
            return redirect('book_list')

        except ValueError:
            messages.error(request, 'Invalid return date format. Please use YYYY-MM-DDTHH:MM format.')
            return redirect('/')
        except Exception as e:
            messages.error(request, f'Error processing return: {str(e)}')
            return redirect('/')
