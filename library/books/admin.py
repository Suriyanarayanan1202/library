from django.contrib import admin
from .models import book_models
from customer.models import customer_model

admin.site.register(book_models)
admin.site.register(customer_model)