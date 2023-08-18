from rest_framework import generics
from rest_framework.response import Response
from .models import Search
from .serializers import SearchSerializer
import requests
from bs4 import BeautifulSoup
import csv
import os
from django.shortcuts import render


class SearchList(generics.ListCreateAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_directory = os.path.dirname(__file__)
        self.search_results = []

        self.load_keywords_and_websites()
        self.perform_search()

    def load_keywords_and_websites(self):
        keywords_file_path = os.path.join(
            self.current_directory, 'keywords.csv')
        websites_file_path = os.path.join(
            self.current_directory, 'websites.csv')

        self.keywords = []
        with open(keywords_file_path, 'r') as keywords_file:
            keywords_reader = csv.reader(keywords_file)
            next(keywords_reader)  # Skip header row
            self.keywords = [row[0] for row in keywords_reader]

        with open(websites_file_path, 'r') as websites_file:
            websites_reader = csv.reader(websites_file)
            next(websites_reader)  # Skip header row
            self.websites = [row[0] for row in websites_reader]

    def perform_search(self):
        for keyword in self.keywords:
            for website_url in self.websites:
                search_result = self.scrape_and_check_keyword(
                    website_url, keyword)
                self.search_results.append(search_result)

        self.save_results_to_csv()

    def scrape_and_check_keyword(self, website_url, keyword):
        try:
            response = requests.get(website_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            relevant_elements = soup.find_all(
                ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            keyword_found = any(keyword in element.get_text()
                                for element in relevant_elements)
            relative_info = "\n".join(
                [element.get_text() for element in relevant_elements if keyword in element.get_text()])

            return {
                'website_url': website_url,
                'keyword': keyword,
                'keyword_found': keyword_found,
                'relative_info': relative_info,
            }
        except requests.exceptions.RequestException:
            return {
                'website_url': website_url,
                'keyword': keyword,
                'keyword_found': False,
                'relative_info': "",
            }

    def save_results_to_csv(self):
        output_file_path = os.path.join(
            self.current_directory, 'search_results.csv')

        with open(output_file_path, 'w', newline='') as output_file:
            fieldnames = ['website_url', 'keyword',
                          'keyword_found', 'relative_info']
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(self.search_results)


def landing_page(request):
    return render(request, 'scraping_app/home.html')
