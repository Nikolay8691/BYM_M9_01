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
	house = checkup.house
	aparts = house.from_house.all()
	results = CheckupResults.objects.filter(checkup = checkup)
	return render(request, 'campaigns/checkup.html', {
		'checkup' : checkup,
		'results' : results,
		'aparts' : aparts,
		})

def add_result(request, checkup_id):

	checkup = Checkup.objects.get(pk = checkup_id)
	house = checkup.house
	aparts = house.from_house.all()
	checkupresult_list = checkup.reason.all()

	s1 = set()
	for c in checkupresult_list:
		s1.add(c.apart)
	s2 = set()
	for a in aparts:
		s2.add(a)
	s2 -= s1
	if len(s2) > 0:
		message = True
	else:
		message = False

	if request.method == 'POST':
		apart = Apartment.objects.get(pk=int(request.POST['apart']))
		c_date = request.POST['c_date']

		# open_door = request.POST['open_door']
		open_door = request.POST.get('open_door',False)

		opinion = request.POST['opinion']
		c_name = request.POST['c_name']
		c_phone = request.POST['c_phone']
		comments = request.POST['comments']

		if open_door == 'on':
			open_door = True
		else:
			open_door = False

		checkupresult = CheckupResults(checkup = checkup, apart = apart, c_date = c_date, open_door = open_door, opinion = opinion, c_name = c_name, c_phone = c_phone, comments = comments)
		checkupresult.save()

		# return HttpResponseRedirect(reverse('campaigns:cu_index'))
		return HttpResponseRedirect(reverse('campaigns:checkup', args = (checkup.id,)))		

	return render(request, 'campaigns/add_result.html', {
		'checkup' : checkup,
		# 'extra_aparts' : aparts,
		'extra_aparts' : s2,
		'checkupresult_list' : checkupresult_list,
		'message' : message,
		})

def stat_index(request):
	campaigns = Campaign.objects.all()
#
	c_sum = len(campaigns)
	if c_sum > 0:

		message_0 = f'detected {c_sum} campaigns'

		sum_1 = c_sum
		message_1 = [[0, 0] for i in range(sum_1)]
		i_1 = 0
		
		c_opens = {}
		c_opinions ={}
		for campaign in campaigns:

			x = 0

			x_positive = 0 
			x_neutral = 0 
			x_negative = 0

			c_opens [str(campaign.id)] = x
			c_opinions [str(campaign.id)] = [x_positive, x_neutral, x_negative]
			c_houses = 0
			houses = campaign.c_objects.all()
			checkups = campaign.departures.all()

			h_sum = len(houses)
			message_1[i_1] = [campaign.id, h_sum]
			i_1 += 1
			
			if h_sum > 0:

				sum_2 = c_sum + h_sum
				message_2 = [[0, 0, 0] for j in range(sum_2)]
				i_2 = 0

				h_opens = {}
				h_opinions ={}
				for house in houses:
					# c_houses += 1

					a = [campaign.id, house.id]
					b = f'campaign_id : {campaign.id} house_id : {house.id}'

					y = 0
					y_positive = 0
					y_neutral = 0
					y_negative = 0
					h_checkups = 0

					h_opens [b] = [a, y]
					h_opinions [b] = [a, y_positive, 0, y_neutral, 0, y_negative, 0]
					
					checkups = checkups.filter(house = house)
					ch_sum = len(checkups)

					message_2[i_2] = [campaign.id, house.id, ch_sum]
					i_2 += 1
					
					if ch_sum > 0:
						c_houses += 1

						sum_3 = c_sum + h_sum + ch_sum
						message_3 = [[0, 0, 0, 0] for k in range(sum_3)]
						i_3 = 0

						for checkup in checkups:
							# h_checkups += 1
							ch_opens = 0

							results = checkup.reason.all()
							res_sum = len(results)

							message_3[i_3] = [campaign.id, house.id, checkup.id, res_sum]
							i_3 += 1
							
							if res_sum > 0:
								h_checkups += 1

								d_sum = 0
								d_open = 0
								positive_sum = 0
								neutral_sum = 0
								negative_sum = 0
								for result in results:
									d_sum += 1

									if result.open_door :
										d_open += 1

										if result.opinion == 'positive':
											positive_sum += 1
										elif result.opinion == 'neutral':
											neutral_sum += 1
										else:
											negative_sum += 1

								ch_opens = d_open/d_sum
								y += ch_opens

								ch_positive = positive_sum/d_sum
								ch_neutral = neutral_sum/d_sum
								ch_negative = negative_sum/d_sum

								y_positive += ch_positive
								y_neutral += ch_neutral
								y_negative += ch_negative

							else:
								print (f'no results detected in campaign {campaign.id} : {campaign.title} in house {house.id} : {house.city} in checkup {checkup.id}')
						
						# print('1c_id ',campaign.id, ' h_id ',house.id, ' ch_id ', checkup.id, ' y ', y, ' h_checkups ',h_checkups)
						if h_checkups == 0:
							c_houses -= 1

						# h_opens += ch_opens/h_checkups
						h_opens [b] = [a, y/h_checkups*100]
						h_opinions [b] = [
							a, 
							round(y_positive/h_checkups*100, 2), positive_sum,
							round(y_neutral/h_checkups*100, 2), neutral_sum,
							round(y_negative/h_checkups*100, 2), negative_sum 
						]
						x += y/h_checkups

						x_positive += y_positive/h_checkups
						x_neutral += y_neutral/h_checkups
						x_negative += y_negative/h_checkups
						# print('c_id ',campaign.id, ' h_id ',house.id, ' ch_id ', checkup.id, ' y ', y, ' h_checkups ',h_checkups)

					else:
						print (f'no checkups detected in campaign {campaign.id} : {campaign.title} in house {house.id} : {house.city}')

				# print(campaign.id, x, c_houses)
				if c_houses > 0:
					c_opens[str(campaign.id)] = round(x/c_houses*100)
					# c_opens[str(campaign.id)] = h_opens/c_houses

					c_opinions[str(campaign.id)] = [
						round(x_positive/c_houses*100),
						round(x_neutral/c_houses*100),
						round(x_negative/c_houses*100)
					]
				else:
					c_opens[str(campaign.id)] = 0
				

			else:
				print (f'no houses detected in campaign {campaign.id} : {campaign.title}')

	else:
		message_0 = f'no campaigns detected'
		print('no campaigns detected')


	return render(request, 'campaigns/stat_index.html', {
		'campaigns' : Campaign.objects.all(),
		'houses' : House.objects.all(),
		'checkups' : Checkup.objects.all(),
		'checkupresults' : CheckupResults.objects.all(),
		'message_0' : message_0,
		'message_1' : message_1,
		'message_2' : message_2,
		'message_3' : message_3,
		'houses_open' : h_opens,
		'houses_opinions' : h_opinions,
		'campaigns_open' : c_opens,
		'campaigns_opinions' : c_opinions,
		})