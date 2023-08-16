from rest_framework import generics, status
from rest_framework.response import Response
from .models import Website, Keyword, SearchResult
from .serializers import WebsiteSerializer, KeywordSerializer, SearchResultSerializer
import requests
from bs4 import BeautifulSoup


class WebsiteList(generics.ListCreateAPIView):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

    def perform_create(self, serializer):
        serializer.save()


class KeywordList(generics.ListCreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class SearchResultsList(generics.ListCreateAPIView):
    queryset = SearchResult.objects.all()
    serializer_class = SearchResultSerializer

    def create(self, request, *args, **kwargs):
        keyword_name = request.data.get('keyword_name')

        try:
            keyword = Keyword.objects.get(name=keyword_name)
            websites = Website.objects.all()
            search_results = []

            for website in websites:
                keyword_found = self.scrape_and_check_keyword(
                    website.url, keyword_name)

                search_result = {
                    'website': website.id,
                    'keyword': keyword.id,
                    'keyword_found': keyword_found,
                    'relative_info': "Relevant info related to the keyword",
                }
                search_results.append(search_result)

            serializer = self.get_serializer(data=search_results, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Keyword.DoesNotExist:
            return Response({'detail': 'Keyword not found'}, status=status.HTTP_400_BAD_REQUEST)

    def scrape_and_check_keyword(self, url, keyword):
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            relevant_elements = soup.find_all(
                ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            for element in relevant_elements:
                if keyword in element.get_text():
                    return True

            return False

        except requests.exceptions.RequestException as e:
            # Handle connection or request errors
            return False
