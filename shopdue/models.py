from django.db import models
import uuid
import os
from datetime import date
# Create your models here.
def generate_unique_filename(instance, filename):
    # Get the original file extension
    extension = os.path.splitext(filename)[1]

    # Generate a unique filename using UUID4
    unique_filename = f"{uuid.uuid4()}{extension}"

    # Return the new path
    return os.path.join("profiles/", unique_filename)


class Customer(models.Model):
    customer_name = models.CharField(max_length=60)
    customer_address = models.TextField()
    contact_number = models.CharField(max_length=12)
    additional_info = models.TextField()
    customer_image = models.ImageField(upload_to=generate_unique_filename, null=True)
    total_due = 0

    def __str__(self) -> str:
        return self.customer_name


class Bill(models.Model):
    customer = models.ForeignKey(Customer, related_name='bills' , on_delete=models.CASCADE)
    invoice_no = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True, null=True)
    discount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    paid = models.FloatField(default=0)
    due = models.FloatField(default=0)



class Purchase(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.TextField()
    price = models.FloatField()
    quantity = models.FloatField()

    @property
    def total(self):
        return self.price * self.quantity
