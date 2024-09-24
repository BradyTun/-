from rest_framework import serializers
from .models import *


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


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['email', 'name', 'phone', 'screenshot',
                  'ticket_type', 'coupon_code']  # Add coupon_code

    def validate(self, data):
        screenshot = data.get('screenshot')
        coupon_code = data.get('coupon_code')

        # Ensure that either screenshot or coupon code is provided, but not both
        if not screenshot and not coupon_code:
            raise serializers.ValidationError(
                "You must provide either a payment screenshot or a valid coupon code.")

        if screenshot and coupon_code:
            raise serializers.ValidationError(
                "You cannot provide both a screenshot and a coupon code. Choose one.")

        # Validate coupon code if provided
        if coupon_code:
            try:
                coupon = CouponCode.objects.get(code=coupon_code)
                if coupon.is_redeemed:
                    raise serializers.ValidationError(
                        'This coupon code has already been redeemed.')
                if coupon.ticket_type != data.get('ticket_type'):
                    raise serializers.ValidationError(
                        'Coupon code is not valid for the selected ticket type.')
            except CouponCode.DoesNotExist:
                raise serializers.ValidationError('Invalid coupon code.')

        return data
