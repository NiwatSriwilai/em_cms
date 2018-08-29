from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', view = views.index, name='index'),
    path('about/', view = views.about, name='about'),
    path('about2/', view = views.about, name='about2'),
    #url('', views.HomePageView.as_view()),
    #url('/about', views.AboutPageView.as_view()),
]
#python manage.py migrate
