from django.db import models
from customer.models import *
from django.utils import timezone

class book_models(models.Model):
    title = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=200,null=True)
    isbn = models.CharField(max_length=200,null=True)
    publisher = models.CharField(max_length=200,null=True)
    pages = models.IntegerField(default=0)
    book_price = models.IntegerField(default=0)
    avaiable = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class transaction_model(models.Model):
    book  = models.ForeignKey(book_models,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer_model,on_delete=models.CASCADE)
    issue_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True, blank= True)
    fee = models.DecimalField(max_digits=5 , default=0,decimal_places=2)

    def __str__(self):
        return "Book Name : " + self.book_models.title + "Member Name : " + self.customer_model.fullname