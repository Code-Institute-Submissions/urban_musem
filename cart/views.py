from django.shortcuts import render, get_object_or_404, redirect, reverse
from donations.models import donation
from models import CartItem
from django.contrib.auth.decorators import login_required
from payments.forms import MakeDonationForm
from django.contrib import messages
from django.template.context_processors import csrf
from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET


# Create your views here.

@login_required(login_url="log_in")
def cart_user(request):
    cartItems = CartItem.objects.filter(user=request.user)
    total = 0
    for item in cartItems:
        total += item.quantity * item.donation.price

    if request.method == 'POST':
        form = MakeDonationForm(request.POST)
        if form.is_valid():
            try:
                contributor = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError, e:
                messages.error(request, 'Your card was declined')

            if contributor.paid:
                messages.success(request, 'You have successfully paid')
                CartItem.objects.filter(user=request.user).delete()
                return redirect(reverse('donations'))
            else:
                messages.error(request, 'Unable to take your payment')
        else:
            messages.error(request, 'We were unable to take your payment with that card')

    else:
        if len(cartItems) == 0:
            return render(request, 'empty_cart.html')
        form = MakeDonationForm()

    args = {'form':form,
            'items': cartItems,
            'total': total,
            'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'cart.html', args)

@login_required(login_url="/log_in")
def add_to_cart(request, id):
    add_donation=get_object_or_404(donation, pk=id)
    quantity=int(request.POST.get('quantity'))
    try:
        cartItem = CartItem.objects.get(user=request.user, donation=add_donation)
        cartItem.quantity += quantity
    except CartItem.DoesNotExist:
        cartItem = CartItem(
            user= request.user,
            donation= add_donation,
            quantity= quantity,
        )
    cartItem.save()
    return redirect(reverse('cart_user'))

def remove_from_cart(request, id):
    CartItem.objects.get(id=id).delete()
    return redirect(reverse('cart_user'))

