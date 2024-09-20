from rest_framework import serializers
from .models import Ticket, PaymentMethod, CustomDonation

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['email', 'name', 'phone', 'screenshot', 'ticket_type']

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['name', 'account', 'description']


class CustomDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomDonation
        fields = ['email', 'phone', 'screenshot', 'amount']
