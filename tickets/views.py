from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError


class TicketSubmissionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        coupon_code = serializer.validated_data.get('coupon_code')
        if coupon_code:
            try:
                coupon = CouponCode.objects.get(code=coupon_code)
                if coupon.is_redeemed:
                    raise ValidationError(
                        'This coupon code has already been redeemed.')
                if coupon.ticket_type != serializer.validated_data.get('ticket_type'):
                    raise ValidationError(
                        'Coupon code is not valid for the selected ticket type.')
            except CouponCode.DoesNotExist:
                raise ValidationError('Invalid coupon code.')

        # Perform the save if validations pass
        serializer.save()

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list':
            # Allow unauthenticated users to submit and query
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]


class CustomDonationViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomDonation.objects.all()
    serializer_class = CustomDonationSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list':
            # Allow unauthenticated users to submit and queru
            return [AllowAny()]
        return [IsAuthenticatedOrReadOnly()]


class PaymentMethodQueryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
