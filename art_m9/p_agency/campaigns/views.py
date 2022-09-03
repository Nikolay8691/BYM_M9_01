from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Campaign, House, Supervisor

# Create your views here.
def index(request):
#
	return render(request, 'campaigns/index.html', {
		'campaigns' : Campaign.objects.all()
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
		})

def h_index(request):
	return render(request, 'campaigns/h_index.html', {
		'houses' : House.objects.all()
		})	

def house(request, house_id):
	house = House.objects.get(pk=house_id)
	return render(request, 'campaigns/house.html', {
		'house' : house,
		# 'apartments' : house.from_house.all(),
		'campaigns' : house.campaigns.all(),
		})

def add(request):

	if request.method == 'POST':

		# user = User.objects.get(pk = user20_id)
		title = request.POST['title']
		status = request.POST['status']
		supervisor = Supervisor.objects.get(pk=int(request.POST['supervisor']))
		campaign = Campaign(title = title, status = status, supervisor = supervisor)
		campaign.save()

		return HttpResponseRedirect(reverse('campaigns:index'))

	else:
		return render(request, 'campaigns/add.html', {
			'supervisors' : Supervisor.objects.all()
			})