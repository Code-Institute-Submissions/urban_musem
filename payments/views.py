from forms import MakeDonationForm
from donations.models import donation
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages, auth
from django.conf import settings
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

import stripe

stripe.api_key = settings.STRIPE_SECRET


# Create your views here.

@login_required(login_url="/login?next=support_us/thanks_for")
def support_us(request, id):
    if request.method == 'POST':
        form = MakeDonationForm(request.POST)
        if form.is_valid():
            try:
                donations = get_object_or_404(donation, pk=id)
                contributor = stripe.Charge.create(
                    amount = int(donations.price * 100),
                    currency = 'EUR',
                    description = donations.title,
                    card = form.cleaned_data['stripe_ide'],
                )
            except stripe.error.CardError, e:
                messages.error(request, 'Your card was declined')

            if contributor.paid:
                messages.success(request, "You have successfully paid")
                return redirect(reverse('home'))
            else:
                messages.error(request, "Unable to take your payment")
        else:
            messages.error(request, "Unable to take your payment with that card")
    else:
        form = MakeDonationForm()
        donations = get_object_or_404(donation, pk=id)
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE, 'donations': donations}
    args.update(csrf(request))
    return render(request, 'support_us.html', args)

