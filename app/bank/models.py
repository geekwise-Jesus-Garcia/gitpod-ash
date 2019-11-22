from django.db import models
import uuid
# Create your models here.

class Branch(models.Model):
    location_name = models.CharField(max_length=100,default='n/a')
    location = models.CharField(max_length=400,default='n/a')
    location_id = str(uuid.uuid4())

    def __str__(self):
        return(f"Bank Name {self.location_name} - location{self.location}")



class Customer(models.Model):
  branch = models.ForeignKey(
    Branch,
    on_delete = models.CASCADE,
  )

  customer_name = models.CharField(max_length=200)

  def __str__(self):
    return(f" Customer Name - {self.customer_name}")


class Account(models.Model):
  branch = models.ForeignKey(
    Branch,
    on_delete = models.CASCADE,
  )
  account_options = (
    ('account', 'Account'),
    ('checking', 'Checking'),
    ('balance', 'Balance'),
  )
 
  product_username = models.CharField(max_length=40)
  product_email = models.EmailField(max_length=400)
  product_options = models.CharField(max_length=8,
    choices=account_options,
    default=account_options[0],
  )

  def __str__(self):
    return(f"Account Name {self.product_username} - Account Email - {self.product_email}")


class Product(models.Model):
  place = models.OneToOneField(
    Branch,
    on_delete=models.CASCADE,
    primary_key=True,
  )

  product_options= (
    ('checking', 'CHECKING'),
    ('saving', 'SAVINGS'),
    ('credit', 'CREDIT'),
  )

  product_options = models.CharField(max_length=40)
  product = models.EmailField(max_length=400)
  product_options = models.CharField(max_length=8)



