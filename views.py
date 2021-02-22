from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import contact_details
from django.core.mail import BadHeaderError, send_mail


def new_contact( request):
	if request.method == 'POST': 
		form = ContactDetailForm(request.POST, request.FILES) 
		if form.is_valid(): 
			form.save()
			return redirect('contact_book:index')
	else: 
		form = ContactDetailForm() 
	return render(request, 'contact_book/add.html', {'form' : form})

def index(request):
	latest_contact_list = contact_details.objects.order_by('-id')[:5]
	context = {'latest_contact_list': latest_contact_list}
	return render(request, 'contact_book/index.html', context)

def submit_contact(request):
	if request.method =='POST':
		profile = ContactDetailForm(request.POST, request.FILES)
		if profile.is_valid(): 
			profile.save() 
			return redirect('success') 
		return HttpResponseRedirect('contact_book/index.html')

def image_upload_view(request):
    if request.method == 'POST':
        profile = ContactDetailForm(request.POST, request.FILES)
        if profile.is_valid(): 
            profile.save() 
            return redirect('success') 
    else: 
        profile = ContactDetailForm() 
    return render(request, 'index.html', {'profile' : profile}) 


def edit_contact(request,id):
	if request.method =='POST':
		selected=contact_details.objects.get(id=id)
		profile = ContactDetailForm(request.POST, instance = selected)
		if profile.is_valid(): 
			profile.save() 
			return redirect('contact_book:index') 
	else:
		selected=contact_details.objects.get(id=id)
		profile = ContactDetailForm(instance=selected)
	return render(request, 'contact_book/edit.html',{'profile':profile})


def delete_contact(request,id):
	contact= contact_details.objects.get(id=id)
	if request.method == 'POST':
		contact.delete()
		return redirect('contact_book:index')
	else:
		messages.error(request,"Something Went Wrong")

def detail_contact(request,id):
	selected=contact_details.objects.get(id=id)
	return render(request, 'contact_book/detail.html',{'contacts':selected})