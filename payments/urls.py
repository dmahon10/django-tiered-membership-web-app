from django.urls import path

from .views import PaymentPageView, pay

urlpatterns = [
    path('', PaymentPageView.as_view(), name='payment'),
    path('pay/', pay, name='pay'),
]
