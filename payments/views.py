import stripe
from django.conf import settings
from django.contrib.auth.models import Permission
from django.shortcuts import render
from django.views.generic.base import TemplateView

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class PaymentPageView(TemplateView): 
    
    template_name = 'payments/purchase.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY 
        return context


def pay(request):
    # Add premium member permissions to user
    permission = Permission.objects.get(codename='premium_member')
    request.user.user_permissions.add(permission)

    if request.method == 'POST':
        stripe.Charge.create(
        amount=3499,
        currency='usd',
        description='Purchase premium membership',
        source=request.POST['stripeToken']
    )
    return render(request, 'payments/payment_confirmation.html')
