from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Ticket, PaymentMethod, CustomDonation
from .serializers import TicketSerializer, PaymentMethodSerializer, CustomDonationSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class TicketSubmissionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list':  
            return [AllowAny()]  # Allow unauthenticated users to submit and queru
        return [IsAuthenticatedOrReadOnly()]  

class CustomDonationViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CustomDonation.objects.all()
    serializer_class = CustomDonationSerializer
    parser_classes = [MultiPartParser, FormParser]  

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list':  
            return [AllowAny()]  # Allow unauthenticated users to submit and queru
        return [IsAuthenticatedOrReadOnly()]  

class PaymentMethodQueryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
