from django.contrib import admin
from django.urls import path
from scraping_app.views import WebsiteList, KeywordList, SearchResultsList

urlpatterns = [
    path("admin/", admin.site.urls),
    path('websites/', WebsiteList.as_view(), name='website-list'),
    path('keywords/', KeywordList.as_view(), name='keyword-list'),
    path('search-results/', SearchResultsList.as_view(),
         name='search-results-list'),
]
