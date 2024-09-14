from django.db import models

class Ticket(models.Model):
    TICKET_TYPES = [
        ('1', 'Programmer Pass - 15,000 MMK'),
        ('2', 'Tech Explorer - 30,000  MMK'),
        ('3', 'Digital Architect - 50,000 MMK'),
        ('4', 'IT Elite - 100,000 MMK')
    ]
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to='payment_screenshots/')
    ticket_type = models.CharField(max_length=4, choices=TICKET_TYPES)

class CustomDonation(models.Model):
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to='payment_screenshots/')
    amount = models.CharField(max_length=12)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=96)
    account = models.TextField()
    description = models.TextField()