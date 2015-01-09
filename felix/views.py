from django.shortcuts import render
from django.core.mail import send_mail
from django import forms
from email.mime.text import MIMEText as text

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

import smtplib
from felix.forms import ContactForm
# import models



def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
	return render(request, 'index.html')

def homepage(request):
	return render(request, 'mainpage.html')

def thanks_page(request):
	return render(request, 'thanks.html')

def receive_message(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data['sender_name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']

			total_message = "".join([email, "\n", message])
			send_mail(sender_name, total_message, email, ['felixmbx@gmail.com'])
			return HttpResponseRedirect('/thanks/')
	else:
		# pass
		form = ContactForm()
	return render(request, 'mainpage.html', {'form' : form})
