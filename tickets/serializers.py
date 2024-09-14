from rest_framework import serializers
from .models import Ticket, PaymentMethod

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['email', 'phone', 'screenshot', 'ticket_type']

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['name', 'account', 'description']
