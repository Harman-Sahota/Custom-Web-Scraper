# from django.test import TestCase
# from .models import Search
# from .views import SearchList
# from rest_framework.test import APIRequestFactory
# import os


# class CustomWebScraperTests(TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()

#     def test_search_list_view(self):
#         response = self.client.get('/search/')

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), len(Search.objects.all()))

#         if len(response.data) > 0:
#             first_result = response.data[0]
#             self.assertIn('website_url', first_result)
#             self.assertIn('keyword', first_result)
#             self.assertIn('keyword_found', first_result)
#             self.assertIn('relative_info', first_result)

#     def test_search_results_saved(self):
#         website_url = 'https://www.example.com/'
#         keyword = 'Example'
#         search_list_view = SearchList()
#         search_result = search_list_view.scrape_and_check_keyword(
#             website_url, keyword)
#         self.assertIsInstance(search_result, dict)
#         self.assertIn('website_url', search_result)
#         self.assertIn('keyword', search_result)
#         self.assertIn('keyword_found', search_result)
#         self.assertIn('relative_info', search_result)

#     def test_search_results_saved_to_csv(self):
#         website_url = 'https://www.example.com/'
#         keyword = 'Example'
#         search_list_view = SearchList()
#         search_result = search_list_view.scrape_and_check_keyword(
#             website_url, keyword)
#         self.assertIsInstance(search_result, dict)
#         search_instance = Search(
#             website_url=website_url,
#             keyword=keyword,
#             keyword_found=search_result['keyword_found'],
#             relative_info=search_result['relative_info']
#         )
#         search_instance.save()
#         saved_search = Search.objects.get(website_url=website_url)
#         self.assertEqual(saved_search.keyword, keyword)

#     def test_csv_file_created(self):
#         search_list_view = SearchList()
#         search_list_view.save_results_to_csv()
#         output_file_path = os.path.join(
#             search_list_view.current_directory, 'search_results.csv')
#         self.assertTrue(os.path.exists(output_file_path))
