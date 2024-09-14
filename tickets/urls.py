from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TicketSubmissionViewSet, PaymentMethodQueryViewSet

router = DefaultRouter()

# Register the custom viewsets
router.register(r'tickets', TicketSubmissionViewSet, basename='ticket-submission')
router.register(r'payment-methods', PaymentMethodQueryViewSet, basename='paymentmethod-query')

urlpatterns = [
    path('api/', include(router.urls)),
]
