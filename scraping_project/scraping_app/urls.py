from django.urls import path
from .views import landing_page, website_list_view, create_website, KeywordSearch, search_websites, scrape_website_content

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('WebsiteList/', website_list_view, name='website_list_view'),
    path('KeywordSearch/', KeywordSearch, name='KeywordSearch'),
    path('api/create-website/', create_website,
         name='api_create_website'),
    path('api/website-search/', search_websites,
         name='api_search_websites'),
    path('api/website-scrape/', scrape_website_content,
         name='api_scrape_websites'),

]
