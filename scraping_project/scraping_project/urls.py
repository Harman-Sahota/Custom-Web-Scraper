from django.urls import path
from scraping_app.views import SearchList

urlpatterns = [
    path('search/', SearchList.as_view(), name='search-list'),
]
