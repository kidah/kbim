from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .services import three_legged_token, respond
from .models import AutodeskAPIs, AutodeskTokens
from django.template import loader
from . import models
from .forms import ChatForm
import json
import logging, urllib
import datetime
# Create your views here.

def index(request):
    return render(request, 'kbim/test.html')

def home(request):
    reply = ''
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            question = request.POST['message']
            reply = respond(question)
            return render(request, 'kbim/index.html', {'form': form,'reply': reply, 'question': question})
    else:
        form =  ChatForm()
        question = ''
    return render(request, 'kbim/index.html', {'form':form, 'reply': reply, 'question': question})

def details(request, api_name):
    template = loader.get_template('kbim/details.html')
    context = {'api_name': api_name.upper()}
    return HttpResponse(template.render(context, request) )

def chat(request, api_name):
    form =  ChatForm()
    template = loader.get_template('kbim/chat.html')
    context = {'api_name': api_name.upper(), 'form': form}  
    return HttpResponse(template.render(context, request) )

def get_message(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            reply = respond(form['message'])
            
            return render(request, 'kbim/index.html', {'reply': reply})
    else:
        form =  ChatForm()
    return render(request, 'kbim/index.html', {'form': form})

     
def getAuthenticationCode(request): 
    return redirect("https://developer.api.autodesk.com/authentication/v1/authorize?response_type=code&client_id=6iJdE4Buo9PhkD4B9EV9zLnMgWf8kZUW&redirect_uri=http%3A%2F%2Flocalhost:8000/kbim/oauth/callback&scope=data:read")


def authenticate(request):
    code = request.GET.get('code')
    response = three_legged_token(code)
    access_granted = False
    #responses = json.loads(three_legged_token(code))
    if response:
        token = AutodeskTokens(
            access_token = response['access_token'],
            refresh_token = response['refresh_token'],
            token_type =  response['token_type'],
            expires_in = datetime.datetime.now() + datetime.timedelta(minutes=60)
            )
        token.save()
        access_granted = True
        return redirect('/kbim/home', { 'access_granted':access_granted})
    return HttpResponse("Access to BIM360 app not granted")
 
 #output = "hello"
    ##logging.info("i got here")
   # response = urllib.request.urlopen("https://developer.api.autodesk.com/authentication/v1/authorize?response_type=code&client_id=6iJdE4Buo9PhkD4B9EV9zLnMgWf8kZUW&redirect_uri=http%3A%2F%2Flocalhost:8000/kbim&scope=data:read").read()
   # logging.info("we got here")
   # return render('kbim/test.html', {'output': response})"""

