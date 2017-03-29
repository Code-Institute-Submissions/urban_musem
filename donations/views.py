from django.shortcuts import render
from models import donation
from django.template.context_processors import csrf

# Create your views here.

def all_donations(request):
    donations = donation.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, 'donations.html', {'donations': donations}, args)