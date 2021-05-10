from django.urls import path
from .views import Charge, Pay, Success


urlpatterns = [
    path("", Pay.as_view(), name="pay"),  # Payment Button Page
    path("charge", Charge.as_view(), name="charge"),  # Razorpay integration
    path("success", Success.as_view(), name="success"),  # Successful Payment
]
