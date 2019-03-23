from django.urls import path
from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('shops/<int:pk>/', views.ShopsViewSet.as_view()),
    url(r'^shops2/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
    url(r'^test_api/', views.SomethingAPIView.as_view(),name='test_api'),
    #url(r'^test_url/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.testUrl),
    #path('shops/', ListShopView.as_view(), name="shops-all")
    #path('about2/', view = views.about, name='about2'),
    #path('callback/', view = views.callback, name='callback'),
    #url('', views.HomePageView.as_view()),
    #url('/about', views.AboutPageView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
