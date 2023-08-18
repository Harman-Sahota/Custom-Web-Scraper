from django.urls import path
from scraping_app.views import SearchList, landing_page

urlpatterns = [
    path('search/', SearchList.as_view(), name='search-list'),
    path('', landing_page, name='landing_page'),
]
