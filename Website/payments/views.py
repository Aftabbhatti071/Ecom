
# payments/views.py
from Ecom.models import Cart
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import PaymentForm
from .models import Payment
from Ecom.models import Cart
import datetime
stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(request):
    user = request.user   
    carts = Cart.objects.filter(user=user)
    amount = 0
    shipping = 0
    if carts:
        for cart_item in carts:
            total_price = cart_item.price * cart_item.quantity
            shipping += cart_item.quantity * 10
            amount += total_price
    total_amount = shipping + amount
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = int(total_amount)
            cardholder = form.cleaned_data['cardholder']
            stripe_token = form.cleaned_data['stripe_token']

            try:
                charge = stripe.Charge.create(
                    amount=amount,
                    currency='usd',
                    description=f'Shopping payment by {request.user.username}',
                    source=stripe_token,
                )
                
                stripe_charge_id = charge['id']
                if Payment.objects.filter(user=user).exists():
                    Payment.objects.filter(user=user).delete()

                Payment.objects.create(
                    user=user,
                    amount=amount,
                    cardholder=cardholder,
                    stripe_charge_id=stripe_charge_id,
                    created_at=datetime.datetime.now(),
                )
                
                return redirect('checkout_complete')
            except :
                return render(request, 'payments/error.html')
    else:
        form = PaymentForm()
    return render(request, 'payments/payment.html', {'form': form, 'total_amount': total_amount, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})




def success_view(request):
    return render(request, 'payments/success.html')





