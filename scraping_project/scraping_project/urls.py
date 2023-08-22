from django.urls import path
from scraping_app.views import landing_page

urlpatterns = [
    path('', landing_page, name='landing_page'),
    # path('scrape/', scrape, name='scrape'),
]
