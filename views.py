from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("welcome to my website")
def setsession(request):
    request.session['name']='alan'
    request.session['email']='alan013@gmail.com'
    return HttpResponse("session set")
def getsession(request):
    name=request.session['name']
    email=request.session['email']
    return HttpResponse(name+' '+email)
def setcookie(request):
    responce=HttpResponse('cookie is set')
    responce.set_cookie('email',alan013@gmail.com)
    return responce
def getcookie(request):
    email=request.COOKIES['email']
    return HttpResponse(email)
# Create your views here.
