from django.shortcuts import render, redirect
from django.template import loader
from django.template.response import TemplateResponse
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.http import Http404

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def index(request):

    context = {
        'home':"home"
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def about(request):
    
    context = {
        'about':"About"
    }

    template = loader.get_template('pages/about.html')
    return HttpResponse(template.render(context, request))

def service(request):
    
    context = {
        'service':"Service"
    }

    template = loader.get_template('pages/service.html')
    return HttpResponse(template.render(context, request))

def realisation(request):
    
    context = {
        'realisation':"Realisation"
    }

    template = loader.get_template('pages/realisation.html')
    return HttpResponse(template.render(context, request))

def contact(request):

    subject, from_email, to = request.POST.get('subject',""), request.POST.get('from_email',""), "michmav28@gmail.com"
    text_content = request.POST.get('message',"")
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.send()