from django.shortcuts import render

from .models import Campaign

# Create your views here.
def index(request):
#
	return render(request, 'campaigns/index.html', {
		'campaigns' : Campaign.objects.all()
		})

def campaign(request, campaign_id):
	campaign = Campaign.objects.get(pk=campaign_id)
	return render(request, 'campaigns/campaign.html', {
		'campaign' : campaign,
		# 'houses' : campaign.c_objects.all(),
		# 'extra_houses' : House.objects.exclude(campaigns=campaign).all(),
		})
