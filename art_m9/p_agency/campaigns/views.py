from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Campaign, House, Supervisor, Checkup, Apartment, CheckupResults

from django.contrib.auth.models import User

# Create your views here.
def index(request):
#
	return render(request, 'campaigns/index.html', {
		'campaigns' : Campaign.objects.all(),
		})

def index2(request):
#
	return render(request, 'campaigns/index2.html', {
		'campaigns' : Campaign.objects.all(),
		'houses2' : House.objects.all(),
		})

def campaign(request, campaign_id):
	campaign = Campaign.objects.get(pk=campaign_id)
	return render(request, 'campaigns/campaign.html', {
		'campaign' : campaign,
		'houses' : campaign.c_objects.all(),
		'extra_houses' : House.objects.exclude(campaigns=campaign).all(),
		'checkups' : campaign.departures.all()
		})

def h_index(request):
	return render(request, 'campaigns/h_index.html', {
		'houses' : House.objects.all(),
		})	

def h2_index(request, user2_id):
	user2 = User.objects.get(pk = user2_id)
	return render(request, 'campaigns/h2_index.html', {
		'houses' : House.objects.all(),
		'user2' : user2,
		})	

def house(request, house_id):
	house = House.objects.get(pk=house_id)
	return render(request, 'campaigns/house.html', {
		'house' : house,
		# 'apartments' : house.from_house.all(),
		'campaigns' : house.campaigns.all(),
		})

def indexplususer2(request, user2_id):
	user2 = User.objects.get(pk = user2_id)
#

# 
	return render(request, 'campaigns/indexplususer2.html', {
		'campaigns' : Campaign.objects.all(),
		'supervisors' : Supervisor.objects.all(),
		'user2' : user2,
		})


def add(request, user2_id):

	user2 = User.objects.get(pk = user2_id)
	if request.method == 'POST':

		title = request.POST['title']
		status = request.POST['status']
		supervisor = Supervisor.objects.get(pk=int(request.POST['supervisor']))
		campaign = Campaign(title = title, status = status, supervisor = supervisor, creator = user2)
		campaign.save()

		return HttpResponseRedirect(reverse('campaigns:index'))
		# return HttpResponseRedirect(reverse('campaigns:indexplususer2', args = (user2.id,)))
	# else:
	# 	return render(request, 'campaigns/add.html', {
	# 		'supervisors' : Supervisor.objects.all(),
	# 		'user2' : user2,
	# 		})

def book(request, campaign_id):
	if request.method == 'POST' :
		campaign = Campaign.objects.get(pk=campaign_id)
		house = House.objects.get(pk=int(request.POST['house']))
		house.campaigns.add(campaign)

	return HttpResponseRedirect(reverse('campaigns:campaign', args = (campaign.id,)))	

def cu_index(request):
	return render(request, 'campaigns/cu_index.html', {
		'checkups' : Checkup.objects.all(),
		})

def checkup(request, checkup_id):
	checkup = Checkup.objects.get(pk=checkup_id)
	# house = checkup.house
	# aparts = house.from_house.all()
	results = CheckupResults.objects.filter(checkup = checkup)
	return render(request, 'campaigns/checkup.html', {
		'checkup' : checkup,
		'results' : results,
		})