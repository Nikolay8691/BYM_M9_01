from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm, ProfileForm2

from django.contrib.auth.models import User

from .models import Profile

from campaigns.models import Campaign

# Create your views here.
def index2(request):
	return render(request, 'users/index2.html', {
		'users' : User.objects.all()
		})

def user2(request, user2_id):
	user2 = User.objects.get(pk = user2_id)
	campaigns = Campaign.objects.filter(creator = user2)	
	return render(request, 'users/user2.html', {
		'user2_campaigns' : campaigns,				
		'user2' : user2,
		'message' : 'from user login'
		})


def user20(request, user20_id):
	user20 = User.objects.get(pk = user20_id)
	return render(request, 'users/user20.html', {
		'user20' : user20,
		'message' : 'from user registration'
		})


def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			# return HttpResponseRedirect(reverse('users:index2'))
			return HttpResponseRedirect(reverse('users:user2', args = (user.id,)))
		else:
			return render(request, 'users/login.html', {
				'message' : ' invalid username and/or password '
				})

	return render(request, 'users/login.html')
	

def logout_view(request):
	logout(request)
	return render(request, 'users/login.html', {
		'message' : ' Logged out '
		})

def logout_plus(request):
	logout(request)
	return render(request, 'users/login.html', {
		'message' : ' To create new campaign : 1. log in 2. move to create new campaign^2 '
		})


def registerplus2(request):

    if request.method == "GET":
        return render(
            request, "users/registerplus2.html", {
            'form': CustomUserCreationForm,            
        	})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()            
            login(request, user)

            return HttpResponseRedirect(reverse('users:user20', args = (user.id,)))


def create_profile2(request, user20_id):
	if request.method == 'POST':
		user = User.objects.get(pk = user20_id)
		user_nick = request.POST['nick']
		user_phone = request.POST['phone']
		profile = Profile(user = user, nick = user_nick, phone = user_phone)
		profile.save()
		return render(request, 'users/login.html', {
			'message' : ' 2_Profile is created! '
			})
