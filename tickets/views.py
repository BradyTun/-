from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Ticket, PaymentMethod
from .serializers import TicketSerializer, PaymentMethodSerializer
from rest_framework.parsers import MultiPartParser, FormParser


# Custom viewset to allow only ticket submission (POST) but no retrieval
class TicketSubmissionViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list':  # For POST requests (ticket submission)
            return [AllowAny()]  # Allow unauthenticated users to submit tickets
        return [IsAuthenticatedOrReadOnly()]  # For other actions (if any), require authentication



# Custom viewset to allow only payment method querying (GET) but no other actions
class PaymentMethodQueryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
