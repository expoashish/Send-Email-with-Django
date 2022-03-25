from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.

def mailfunction(request):
	send_mail(
	    'Testing Email',
	    'Hello Bro, How are you?',
	    'expofacts@gmail.com',
	    ['codexashish@gmail.com'],
	    fail_silently=False,
	)
	return render(request, 'index.html')
