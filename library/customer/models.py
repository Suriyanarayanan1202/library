from django.db import models

class customer_model(models.Model):
    fullname = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    outstanding_amount = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.fullname