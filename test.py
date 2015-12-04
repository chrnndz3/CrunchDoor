from crunchDoorApp.models import *
from django.shortcuts import get_object_or_404
import urllib2, sys
from BeautifulSoup import BeautifulSoup
import json
from pprint import pprint

###FOR CRAWLING THE GLASSDOOR API
# for i in range(1,23):
# 	url = "http://api.glassdoor.com/api/api.htm?t.p=49299&t.k=fXqLQtzbYfO&format=json&v=1&action=employers&q=Software&city=San_Francisco&pn=%d"%(i) 
# 	hdr = {'User-Agent': 'Mozilla/5.0'}
# 	print 'URL: %s' % (url)
# 	req = urllib2.Request(url,headers=hdr)
# 	response = urllib2.urlopen(req)
# 	soup = BeautifulSoup(response)
# 	data_file = json.loads(str(soup))
# 	ourResult = data_file['response']['employers'] 
# 	for rs in ourResult:
# 		name = rs['name']
# 		website = rs['website']
# 		total_Reviews = rs['numberOfRatings']
# 		average = rs['overallRating']
# 		logo = rs['squareLogo']
# 		industry = rs['industryName']
# 		c = Company(name=name, 
# 		website=website, total_Reviews=total_Reviews, 
# 		average=average, logo=logo, industry=industry)
# 		c.save()
# 		pprint(name)


###FOR CRAWLING THE CRUNCHBASE API
# for i in range(200,201):
# 	company = Company.objects.get(pk=i)
# 	print company.name
# 	pprint(company.company_id)
# 	companyPermalink = company.name.replace(" ", "-").lower()
# 	# print companyPermalink
# 	url = "https://api.crunchbase.com/v/3/organizations/%s?user_key=daa3c097551d2db8b278f34597499ab9"%(companyPermalink)
# 	print 'URL: %s' % (url)
# 	req = urllib2.Request(url)
# 	response = urllib2.urlopen(req)
# 	soup = BeautifulSoup(response)
# 	data_file = json.loads(str(soup))
# 	ourResult = data_file['data']['properties']['name']
# 	pprint(company.name)
# 	pprint(ourResult)
# 	founded = data_file['data']['properties']['founded_on']
# 	employees = data_file['data']['properties']['num_employees_max']
# 	funding = data_file['data']['properties']['total_funding_usd']
# 	symbol = data_file['data']['properties']['stock_symbol']
# 	extra_id = company.company_id
# 	c = Crunch(crunch_id = company, extra_id = extra_id, permalink = companyPermalink, founded = founded, employees = employees, funding = funding, symbol = symbol)
# 	c.save()
# 	pprint(c)




## DELETE A COMPANY
# company = Company.objects.get(pk=198)
# print company.name
# company.delete()


###Alogrithm for Similar Search
# points = []
# indices = []

# company = get_object_or_404(Company, pk=2)
# currCompany = get_object_or_404(Crunch, crunch_id = company.company_id)
# currCompany_founded = currCompany.founded[0:4]

# for c in Crunch.objects.all():
# 	# company = get_object_or_404(Company,pk = company_id)
# 	# print company.name
# 	# print company.company_id
# 	# print currCompany.extra_id
# 	#funding comparison
# 	if c.extra_id == currCompany.extra_id:
# 		continue
# 	print "-------"
# 	print c.extra_id
# 	print c.permalink
# 	diff = currCompany.funding - c.funding
# 	diff_funding = abs(diff)
# 	# print diff_funding
# 	funding_points = 0
# 	employees_points = 0
# 	reviews_points = 0
# 	founded_points = 0
# 	if diff_funding >= 0 and diff_funding < 50:
# 		funding_points += 5
# 	elif diff_funding >= 100 and diff_funding < 500:
# 		funding_points += 4
# 	elif diff_funding >= 500 and diff_funding < 1000:
# 		funding_points += 3
# 	elif diff_funding >= 1000 and diff_funding < 5000:
# 		funding_points += 2
# 	elif diff_funding >= 5000 and diff_funding < 10000:
# 		funding_points += 1
# 	# print funding_points
# 	if currCompany.employees is not None and c.employees is not None:
# 		diff2 = currCompany.employees - c.employees
# 		diff_employees = abs(diff2)
# 		if diff_employees >= 0 and diff_employees < 50:
# 			employees_points += 5
# 		elif diff_employees >= 100 and diff_employees < 500:
# 			employees_points += 4
# 		elif diff_employees >= 500 and diff_employees < 1000:
# 			employees_points += 3
# 		elif diff_employees >= 1000 and diff_employees < 5000:
# 			employees_points += 2
# 		elif diff_employees >= 5000 and diff_employees < 10000:
# 			employees_points += 1
# 		print employees_points
# 	glasscompany = get_object_or_404(Company, pk=c.extra_id)
# 	diff3 = company.average - glasscompany.average
# 	diff_reviews = abs(diff3)
# 	# print diff_reviews
# 	if diff_reviews == 0.00:
# 		reviews_points += 5
# 	elif diff_reviews <= 0.50:
# 		reviews_points += 4
# 	elif diff_reviews <= 1.00:
# 		reviews_points += 3
# 	elif diff_reviews <= 1.50:
# 		reviews_points += 2
# 	elif diff_reviews <= 2.00:
# 		reviews_points += 1
# 	print reviews_points
# 	if c.founded is not None:
# 		c_founded = c.founded[0:4]
# 		# print c_founded
# 		diff4 = int(currCompany_founded) - int(c_founded)
# 		diff_founded = abs(diff4)
# 		# print diff_founded
# 		# print currCompany_founded
# 		if diff_founded == 0:
# 			founded_points +=5
# 		elif diff_founded < 5:
# 			founded_points +=4
# 		elif diff_founded < 15:
# 			founded_points += 3
# 		elif diff_founded < 25:
# 			founded_points +=2
# 		elif diff_founded < 50:
# 			founded_points +=1
# 	total_points = funding_points+employees_points+reviews_points+founded_points
# 	print total_points
# 	print glasscompany.name
# 	indices.append(c.extra_id)
# 	points.append(total_points)
	


# # b = 0
# # for i in points:
# # 	print i
# # 	print indices[b]
# # 	b += 1

# max1 = -1
# max2 = -1
# max3 = -1
# index = 0
# var1 = -1
# var2 = -1
# var3 = -1
# for i in points:
# 	if i > max1:
# 		max3 = max2
# 		max2 = max1
# 		max1 = i
# 		var3 = var2
# 		var2 = var1
# 		var1 = index
# 	elif i > max2:
# 		max3 = max2
# 		max2 = i
# 		var3 = var2
# 		var2 = index
# 	elif i > max3:
# 		max3 = i
# 		var3 = index
# 	index += 1 

# print max1 # max total_points
# print indices[var1]
# print max2
# print indices[var2]
# print max3
# print indices[var3]# Index of the company that has the max total_points















