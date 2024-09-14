from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TicketSubmissionViewSet, PaymentMethodQueryViewSet, CustomDonationViewSet

router = DefaultRouter()

# Register the custom viewsets
router.register(r'tickets', TicketSubmissionViewSet, basename='ticket')
router.register(r'donate', CustomDonationViewSet, basename='custom-donation')
router.register(r'payment-methods', PaymentMethodQueryViewSet, basename='paymentmethod-query')

urlpatterns = [
    path('', include(router.urls)),
]
