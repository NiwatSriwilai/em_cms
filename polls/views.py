import logging
import webbrowser as wb
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
import requests

def index(request):
    #https://access.line.me/oauth2/v2.1/login?returnUri=%2Foauth2%2Fv2.1%2Fauthorize%2Fconsent%3Fscope%3Dprofile%26response_type%3Dcode%26state%3D12345abcde%26redirect_uri%3Dhttp%253A%252F%252F35.197.130.54%252Fcallback.html%26client_id%3D1594794852&loginChannelId=1594794852&loginState=9pSz0AXSXEaDkgfjaZqfxo
    #wb.open_new_tab('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://35.197.130.54/callback.html')
    render(request, 'index.html', context=None)
    #HttpResponse("Hello, world. xxx")
    #HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponseRedirect('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=openid')
    
def requestCurl():
    data = {
            "grant_type": "authorization_code",
            "code":"fr1FBb3equGxa8QAMVeZ",
            "redirect_uri":"http://niwat.pythonanywhere.com/polls/callback/",
            "client_id":"1594794852",
            "client_secret":"31d3e4e088773ca7feaed23cd5ecc33e"
            }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    data2 = [
      ('grant_type', 'authorization_code'),
      ('code', 'xxx'),
      ('redirect_uri', 'xxx'),
      ('client_id', 'xxx'),
      ('client_secret', 'xxx'),
    ]

    response = requests.post('https://api.line.me/oauth2/v2.1/token', headers=headers, data=data)
    print ('response = '+response.text)
#requestCurl()    
#def about(request):
#    return render(request, 'about.html', context=None)
def callback(request):
    #print(request.GET.get('name', '')+' B = '+request.GET.get('b', ''))
    #return HttpResponse(request.GET['name'])
    #return render(request, 'index.html', context=None)
    #https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=profile
    #http://niwat.pythonanywhere.com/polls/callback/?code=PzM1z4J3qpW9zWaNMx5e&state=12345abcde
    #wb.open('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1594794852&redirect_uri=http://niwat.pythonanywhere.com/polls/callback/&state=12345abcde&scope=profile')
    return render(request, 'about.html', context=None)
        
#class HomePageView(TemplateView):
#    def get(self, request, **kwargs):
#        return render(request, 'about.html', context=None)
#class AboutPageView(TemplateView):
#    template_name = "about.html"
#https://www.quora.com/How-do-I-add-my-Django-projects-on-GitHub#
#https://scotch.io/tutorials/working-with-django-templates-static-files

