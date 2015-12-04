from django.shortcuts import render, get_object_or_404, redirect
import requests
import json
from django.http import Http404, JsonResponse
from django.http import Http404
from django.template import RequestContext, loader
from django.forms import ModelForm
from .models import Company, CrunchMemoized, LocationMemoized, ProductMemoized, Crunch
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class Form(ModelForm):
    class Meta:
        model = Company
        fields = ['company_id','name','website', 'total_Reviews', 'average', 'logo', 'industry']

def home(request):
	return render(request, 'home.html')

def index(request, query, order):
	company_list = Company.objects.filter(Q(name__icontains=query)).order_by(order)
	if query == 'all':
		company_list = Company.objects.order_by(order)
		query = ''
	paginator = Paginator(company_list,10)
	page = request.GET.get('page')
	try:
		company_list = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		company_list = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		company_list = paginator.page(paginator.num_pages)
	order1= order2 = order3 = order4 = ''
	if order == 'name':
		order1 = 'selected'
	if order == '-name':
		order2 = 'selected'
	if order == '-average':
		order3 = 'selected'
	if order == 'average':
		order4 = 'selected'

	context = RequestContext(request, {'company_list': company_list, 'query':query, 'order1':order1, 'order2': order2, 'order3':order3, 'order4': order4})
	output =', '.join([p.name for p in company_list])
	return render(request, 'index.html', context)

def detail(request, company_id):
	company = get_object_or_404(Company,pk = company_id)
	currCompany = get_object_or_404(Crunch, crunch_id = company.company_id)
	companyPermalink = currCompany.permalink
	memoizedCompany = CrunchMemoized.objects.filter(permalink= companyPermalink)
	if not memoizedCompany:
		memoizedCompany = "#000"
		
		r = requests.get("https://api.crunchbase.com/v/3/organizations/"+ companyPermalink +"?user_key=daa3c097551d2db8b278f34597499ab9")
		details = r.json()
		content = json.loads(r.content)
		crunchMemo = CrunchMemoized(permalink = companyPermalink, short_description = content["data"]["properties"]["short_description"])
		crunchMemo.save()
		for location in content["data"]["relationships"]["offices"]["items"]:
			locationMemo = LocationMemoized(permalink = companyPermalink, name = location["properties"]["name"], street_1 = location["properties"]["street_1"], city = location["properties"]["city"])
			locationMemo.save()
		for product in content["data"]["relationships"]["products"]["items"]:
			productMemo = ProductMemoized(permalink = companyPermalink, name = product["properties"]["name"])
			productMemo.save()

	else:
		memoizedCompany = "#27ae60"
		locationMemo = LocationMemoized.objects.filter(permalink = companyPermalink)
		productMemo = ProductMemoized.objects.filter(permalink = companyPermalink)
		crunchMemo = CrunchMemoized.objects.filter(permalink = companyPermalink)[:1].get()

		content = {}
		data = {}
		properties = {}
		relationships = {}
		offices = {}
		products = {}
		content["data"] = data
		data["properties"] = properties
		data["relationships"] = relationships
		relationships["offices"] = offices
		relationships["products"] = products


		content['data']['properties']['short_description'] = crunchMemo.short_description
		locationItems = []
		for location in locationMemo:
			prop = {}
			properties = {}
			prop["properties"] = properties
			properties['name'] = location.name
			properties['street_1'] = location.street_1
			properties['city'] = location.city
			locationItems.append(prop)
		content['data']['relationships']['offices']['items'] = locationItems

		productItems = []
		for product in productMemo:
			prop = {}
			properties = {}
			prop["properties"] = properties
			properties['name'] = product.name
			productItems.append(prop)
		content['data']['relationships']['products']['items'] = productItems


	
	#Create Similar company's algorithm here
	points = []
	indices = []

	
	if currCompany.founded is not None:
		currCompany_founded = currCompany.founded[0:4]


	if currCompany.similarcompany1 == 0:
		for c in Crunch.objects.all():
			# company = get_object_or_404(Company,pk = company_id)
			# print company.name
			# print company.company_id
			# print currCompany.extra_id
			#funding comparison
			if c.extra_id == currCompany.extra_id:
				continue
			diff = currCompany.funding - c.funding
			diff_funding = abs(diff)
			# print diff_funding
			funding_points = 0
			employees_points = 0
			reviews_points = 0
			founded_points = 0
			if diff_funding >= 0 and diff_funding < 50:
				funding_points += 5
			elif diff_funding >= 100 and diff_funding < 500:
				funding_points += 4
			elif diff_funding >= 500 and diff_funding < 1000:
				funding_points += 3
			elif diff_funding >= 1000 and diff_funding < 5000:
				funding_points += 2
			elif diff_funding >= 5000 and diff_funding < 10000:
				funding_points += 1
			# print funding_points
			if currCompany.employees is not None and c.employees is not None:
				diff2 = currCompany.employees - c.employees
				diff_employees = abs(diff2)
				if diff_employees >= 0 and diff_employees < 50:
					employees_points += 5
				elif diff_employees >= 100 and diff_employees < 500:
					employees_points += 4
				elif diff_employees >= 500 and diff_employees < 1000:
					employees_points += 3
				elif diff_employees >= 1000 and diff_employees < 5000:
					employees_points += 2
				elif diff_employees >= 5000 and diff_employees < 10000:
					employees_points += 1
			glasscompany = get_object_or_404(Company, pk=c.extra_id)
			diff3 = company.average - glasscompany.average
			diff_reviews = abs(diff3)
			# print diff_reviews
			if diff_reviews == 0.00:
				reviews_points += 5
			elif diff_reviews <= 0.50:
				reviews_points += 4
			elif diff_reviews <= 1.00:
				reviews_points += 3
			elif diff_reviews <= 1.50:
				reviews_points += 2
			elif diff_reviews <= 2.00:
				reviews_points += 1
			if c.founded and currCompany.founded is not None:
				c_founded = c.founded[0:4]
				# print c_founded
				diff4 = int(currCompany_founded) - int(c_founded)
				diff_founded = abs(diff4)
				# print diff_founded
				# print currCompany_founded
				if diff_founded == 0:
					founded_points +=5
				elif diff_founded < 5:
					founded_points +=4
				elif diff_founded < 15:
					founded_points += 3
				elif diff_founded < 25:
					founded_points +=2
				elif diff_founded < 50:
					founded_points +=1
			total_points = funding_points+employees_points+reviews_points+founded_points
			indices.append(c.extra_id)
			points.append(total_points)

	#getting the top 3 indices and values
		max1 = -1
		max2 = -1
		max3 = -1
		index = 0
		var1 = -1
		var2 = -1
		var3 = -1
		for i in points:
			if i > max1:
				max3 = max2
				max2 = max1
				max1 = i
				var3 = var2
				var2 = var1
				var1 = index
			elif i > max2:
				max3 = max2
				max2 = i
				var3 = var2
				var2 = index
			elif i > max3:
				max3 = i
				var3 = index
			index += 1 

		print max1 # max total_points
		print indices[var1]
		print max2
		print indices[var2]
		print max3
		print indices[var3]# Index of the company that has the max total_points

		##Save the similar companies into database so iteration does not have to happen again
		currCompany.similarcompany1 = indices[var1]
		currCompany.similarcompany2 = indices[var2]
		currCompany.similarcompany3 = indices[var3]
		currCompany.save()

	company_list = []
	company1 = get_object_or_404(Company, pk = currCompany.similarcompany1)
	company2 = get_object_or_404(Company, pk = currCompany.similarcompany2)
	company3 = get_object_or_404(Company, pk = currCompany.similarcompany3)
	company_list.append(company1)
	company_list.append(company2)
	company_list.append(company3)

	return render(request, 'detail.html', {'company': company, 'currCompany':currCompany, 'company_list':company_list, "details":content, "memoized": memoizedCompany})

def update(request, company_id):
	company = get_object_or_404(Company,pk = company_id)
	form = Form(request.POST or None, instance=company)
	if form.is_valid():
		form.save()
		return render(request, 'detail.html', {'company': company})
	return render(request, 'form.html', {'form':form})

def create(request):
	form = Form(request.POST or None)
	if form.is_valid():
		form.save()
		company_list = Company.objects.order_by('-name')[:5]
		context = RequestContext(request, {'company_list': company_list,})
		return render(request, 'index.html', context)
	return render(request, 'form.html', {'form':form})

def delete(request, company_id):
	company = get_object_or_404(Company,pk = company_id)
	if request.method=='POST':
		company.delete()
		company_list = Company.objects.order_by('-name')[:5]
		context = RequestContext(request, {'company_list': company_list,})
		return render(request, 'index.html', context)
	return render(request, 'confirm_delete.html', {'object':company})

def search_companies(request):
	if request.method =="GET":
		search_text = request.GET['search_text']
		if search_text is not None and search_text != u"":
			search_text = request.GET['search_text']
			company_list = Company.objects.filter(Q(name__icontains=search_text)).order_by('-name')[:5]
		else:
			company_list = []
		return render(request, 'index.html', {'company_list':company_list})





