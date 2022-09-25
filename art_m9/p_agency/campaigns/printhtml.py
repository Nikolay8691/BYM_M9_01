from .models import Campaign, House

def c_opens_printhtml(c_opens):
	i = 0
	c1_opens = {}
	for key, value in c_opens.items():

		campaign = Campaign.objects.get(pk=key)
		c1_opens[str(i)] = [campaign.id, campaign.title, value]
		i += 1

	return c1_opens

def h_opens_printhtml(h_opens):
	i = 0
	h1_opens = {}
	for value in h_opens.values():

		data_id, data = value
		campaign = Campaign.objects.get(pk = data_id[0])
		house = House.objects.get(pk = data_id[1])
		h1_opens[str(i)] = [campaign.id, campaign.title, house.id, house.city, data]
		i += 1

	return h1_opens

def c_opinions_printhtml(c_opinions):
	i = 0
	c1_opinions = {}
	for key, value in c_opinions.items():
		positive, neutral, negative = value
		campaign = Campaign.objects.get(pk=key)
		c1_opinions[str(i)] = [campaign.id, campaign.title, positive, neutral, negative]
		i += 1

	return c1_opinions

def h_opinions_printhtml(h_opinions):
	i = 0
	h1_opinions = {}
	for value in h_opinions.values():
		data_id, positive, positive_sum, neutral, neutral_sum, negative, negative_sum = value
		campaign = Campaign.objects.get(pk = data_id[0])
		house = House.objects.get(pk = data_id[1])
		h1_opinions[str(i)] = [campaign.id, campaign.title, house.id, house.city, positive, neutral, negative]
		i += 1

	return h1_opinions
