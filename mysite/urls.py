"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.urls import include, path
#from django.conf.urls import include
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from cms.views import task_router
from cms import views
router = routers.DefaultRouter()
router.register(r'emcms/api/v1/shops', views.ShopsViewSet2)
router.register(r'emcms/api/v1/categories', views.CategoriesViewSet)
router.register(r'emcms/api/v1/cat_shops', views.CategoriesWithShopsViewSet)
#shop_detail = views.ShopsViewSet.as_view({
#    'get': 'retrieve'
#})
urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('cms/', include('cms.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

