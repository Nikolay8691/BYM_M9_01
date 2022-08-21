from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# from .forms import CustomUserCreationForm, ProfileForm, ProfileForm2

from django.contrib.auth.models import User

# from .models import Profile

# Create your views here.
def index2(request):
	return render(request, 'users/index2.html', {
		'users' : User.objects.all()
		})

def user2(request, user2_id):
	user2 = User.objects.get(pk = user2_id)
	return render(request, 'users/user2.html', {
		'user2' : user2,
		'message' : 'from user login'
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

