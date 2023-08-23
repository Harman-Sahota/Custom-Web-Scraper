from django.urls import path
from .views import landing_page, WebsiteList, create_website

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('WebsiteList/', WebsiteList, name='WebsiteList'),
    path('api/create-website/', create_website,
         name='api_create_website'),
]
