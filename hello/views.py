from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.http import Http404
from django.template import RequestContext, loader
from django.forms import ModelForm
from .models import Company
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class Form(ModelForm):
    class Meta:
        model = Company
        fields = ['company_id','name','website', 'total_Reviews', 'average', 'logo', 'industry']

def home(request):
	return render(request, 'crunchDoorApp/home.html')

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
	return render(request, 'crunchDoorApp/index.html', context)

def detail(request, company_id):
	company = get_object_or_404(Company,pk = company_id)
	companyPermalink = company.name.replace(" ", "-").lower()
	r = requests.get("https://api.crunchbase.com/v/3/organizations/"+ companyPermalink +"?user_key=daa3c097551d2db8b278f34597499ab9")
	hey = r.json()
	#Create Similar company's algorithm here
	company_list = Company.objects.order_by('-name')[:3]
	return render(request, 'crunchDoorApp/detail.html', {'company': company, 'company_list':company_list, "details":hey})

def update(request, company_id):
	company = get_object_or_404(Company,pk = company_id)
	form = Form(request.POST or None, instance=company)
	if form.is_valid():
		form.save()
		return render(request, 'crunchDoorApp/detail.html', {'company': company})
	return render(request, 'crunchDoorApp/form.html', {'form':form})

def create(request):
	form = Form(request.POST or None)
	if form.is_valid():
		form.save()
		company_list = Company.objects.order_by('-name')[:5]
		context = RequestContext(request, {'company_list': company_list,})
		return render(request, 'crunchDoorApp/index.html', context)
	return render(request, 'crunchDoorApp/form.html', {'form':form})

def delete(request, company_id):
	company = get_object_or_404(Company,pk = company_id)
	if request.method=='POST':
		company.delete()
		company_list = Company.objects.order_by('-name')[:5]
		context = RequestContext(request, {'company_list': company_list,})
		return render(request, 'crunchDoorApp/index.html', context)
	return render(request, 'crunchDoorApp/confirm_delete.html', {'object':company})

def search_companies(request):
	if request.method =="GET":
		search_text = request.GET['search_text']
		if search_text is not None and search_text != u"":
			search_text = request.GET['search_text']
			company_list = Company.objects.filter(Q(name__icontains=search_text)).order_by('-name')[:5]
		else:
			company_list = []
		return render(request, 'crunchDoorApp/index.html', {'company_list':company_list})





