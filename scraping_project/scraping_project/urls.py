from django.urls import path
from scraping_app.views import landing_page, scrape, create_website

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('scrape/', scrape, name='scrape'),
    path('api/create-website/', create_website,
         name='api_create_website'),
]
