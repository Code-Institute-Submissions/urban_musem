from django.shortcuts import render
from models import donation

# Create your views here.

def all_donations(request):
    donations = donation.objects.all()
    args = {'donations': donations}
    return render(request, 'donations.html', args)