from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from .models import WebsiteList
from .serializers import WebsiteListSerializer
from django.shortcuts import render

# class SearchList(generics.ListCreateAPIView):
#     queryset = Search.objects.all()
#     serializer_class = SearchSerializer

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.current_directory = os.path.dirname(__file__)
#         self.search_results = []

#         self.load_keywords_and_websites()
#         self.perform_search()

#     def load_keywords_and_websites(self):
#         keywords_file_path = os.path.join(
#             self.current_directory, 'keywords.csv')
#         websites_file_path = os.path.join(
#             self.current_directory, 'websites.csv')

#         self.keywords = []
#         with open(keywords_file_path, 'r') as keywords_file:
#             keywords_reader = csv.reader(keywords_file)
#             next(keywords_reader)  # Skip header row
#             self.keywords = [row[0] for row in keywords_reader]

#         with open(websites_file_path, 'r') as websites_file:
#             websites_reader = csv.reader(websites_file)
#             next(websites_reader)  # Skip header row
#             self.websites = [row[0] for row in websites_reader]

#     def perform_search(self):
#         for keyword in self.keywords:
#             for website_url in self.websites:
#                 search_result = self.scrape_and_check_keyword(
#                     website_url, keyword)
#                 self.search_results.append(search_result)

#         self.save_results_to_csv()

#     def scrape_and_check_keyword(self, website_url, keyword):
#         try:
#             response = requests.get(website_url)
#             response.raise_for_status()

#             soup = BeautifulSoup(response.text, 'html.parser')
#             relevant_elements = soup.find_all(
#                 ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

#             keyword_found = any(keyword in element.get_text()
#                                 for element in relevant_elements)
#             relative_info = "\n".join(
#                 [element.get_text() for element in relevant_elements if keyword in element.get_text()])

#             return {
#                 'website_url': website_url,
#                 'keyword': keyword,
#                 'keyword_found': keyword_found,
#                 'relative_info': relative_info,
#             }
#         except requests.exceptions.RequestException:
#             return {
#                 'website_url': website_url,
#                 'keyword': keyword,
#                 'keyword_found': False,
#                 'relative_info': "",
#             }

#     def save_results_to_csv(self):
#         output_file_path = os.path.join(
#             self.current_directory, 'search_results.csv')

#         with open(output_file_path, 'w', newline='') as output_file:
#             fieldnames = ['website_url', 'keyword',
#                           'keyword_found', 'relative_info']
#             writer = csv.DictWriter(output_file, fieldnames=fieldnames)

#             writer.writeheader()
# writer.writerows(self.search_results)


def landing_page(request):
    return render(request, 'scraping_app/home.html')


def website_list_view(request):
    return render(request, 'scraping_app/WebsiteList.html')


@csrf_exempt
@api_view(['POST'])
def create_website(request):
    if request.method == 'POST':
        serializer = WebsiteListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            response_data = {'message': 'Website created successfully'}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    response_data = {'error': 'Invalid request method'}
    return Response(response_data, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def KeywordSearch(request):
    return render(request, 'scraping_app/KeywordSearch.html')


@api_view(['POST'])
def search_websites(request):
    if request.method == 'POST':
        category = request.data.get('category')
        keyword = request.data.get('keyword')

        websites = WebsiteList.objects.filter(category=category)
        search_results = []

        for website in websites:
            result = {
                'website_name': website.website_url,
                'website_url': website.website_url,
            }

            if website.has_data_api:  # Assuming 'has_data_api' is a field in your WebsiteList model
                try:
                    api_url = website.data_api_url
                    response = requests.get(api_url)
                    api_data = response.json()
                    result['api_data'] = api_data
                except requests.exceptions.RequestException as api_request_exception:
                    result['api_error'] = str(api_request_exception)
            else:
                try:
                    scraped_data = scrape_website_content(
                        website.website_url, keyword)  # Pass keyword to the function
                    result['scraped_data'] = scraped_data
                except Exception as e:
                    result['scrape_error'] = str(e)

            search_results.append(result)

        return Response({'search_results': search_results})

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def scrape_website_content(website_url, keyword):
    try:
        response = requests.get(website_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        # Update the CSS selectors to target the relevant elements more accurately
        # Adjust the selectors as needed
        matching_elements = soup.select('h1, h2, h3, p')

        scraped_data = ""
        for element in matching_elements:
            if keyword.lower() in element.get_text().lower():
                scraped_data += element.get_text() + "\n"

        return scraped_data.strip()  # Remove leading/trailing whitespace
    except requests.exceptions.RequestException as request_exception:
        raise Exception(f"Request error: {str(request_exception)}")
    except Exception as e:
        raise Exception(f"Scraping error: {str(e)}")
