from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.models import User



# Create your views here.

def log_out(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('home'))

@login_required(login_url='/log_in')
def profile(request):
    return render(request, 'profile.html')

def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username_or_email'),
                                     password=request.POST.get('password'))
            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfuly logged in")

                if request.GET and 'next' in request.GET:
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('get_discover'))
            else:
                form.add_error(None, 'Your username os password was not recognised')
    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    args.update(csrf(request))

    return render(request, 'log_in.html', args)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))
            if user:
                auth.login(request, user)
                messages.success(request, 'You have succesfully registered')
                return redirect(reverse('get_discover'))
            else:
                messages.error(request, 'Unable to log you in at this time')
    else:
        form = UserRegistrationForm()
    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'register.html', args)

def remove_account(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('home'))
