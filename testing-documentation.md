

# Custom Web Scraper - Testing Documentation

## Introduction

This documentation provides an overview of the testing procedures and unit tests implemented for the Custom Web Scraper project. Unit testing is a crucial aspect of software development that ensures the correctness and reliability of code components.

## Testing Strategy

The testing strategy for the Custom Web Scraper project involves creating unit tests for the key functionalities of the application. These tests are designed to verify the behavior and correctness of individual functions, methods, and views.

## Test Cases

### 1. test_search_list_view

Purpose: This test case verifies that the SearchList API view is functioning correctly and returning the expected response.

Steps:
1. Create a dummy request using the APIRequestFactory.
2. Create a response instance using the SearchList view.
3. Assert that the response status code is 200 (HTTP OK).
4. Assert that the response data contains the expected text "Search Results".

### 2. test_search_results_saved

Purpose: This test case checks whether the scrape_and_check_keyword method is correctly saving search results.

Steps:
1. Define a dummy website URL and keyword.
2. Call the scrape_and_check_keyword method with the dummy URL and keyword.
3. Assert that the returned search result is a dictionary and contains expected keys.
4. Create a dummy Search instance and save it.
5. Retrieve the saved instance and verify that the keyword matches the expected value.

### 3. test_search_results_saved_to_csv

Purpose: This test case ensures that the search results are correctly saved to a CSV file.

Steps:
1. Define a dummy website URL and keyword.
2. Call the scrape_and_check_keyword method with the dummy URL and keyword.
3. Assert that the returned search result is a dictionary and contains expected keys.
4. Create a dummy Search instance and save it.
5. Verify that the CSV file containing search results is created.

### 4. test_csv_file_created

Purpose: This test case verifies that the CSV file is created after saving search results.

Steps:
1. Instantiate the SearchList view.
2. Call the save_results_to_csv method.
3. Assert that the CSV file is created in the expected directory.

### 5. test_api_endpoint

Purpose: This test case verifies that the API endpoint returns the expected JSON data.

Steps:
1. Create a dummy request using the APIRequestFactory.
2. Create a response instance using the SearchList view.
3. Assert that the response status code is 200 (HTTP OK).
4. Assert that the response data contains key information such as website_url, keyword, keyword_found, and relative_info.

## Running Tests

To run the unit tests for the Custom Web Scraper project, follow these steps:

1. Make sure you are in the project directory containing the manage.py script.
2. Open a terminal or command prompt.
3. Run the following command to execute the tests:
```bash
   python manage.py test
```
4. The tests will run, and the results will be displayed in the terminal.
5. Observe the test results. If all tests pass, you should see OK. If there are failures or errors, detailed information will be provided.

## Conclusion

Unit testing is an essential part of the development process, ensuring that each component of the code works as expected and minimizing the chances of introducing bugs. The tests outlined in this documentation provide comprehensive coverage of the Custom Web Scraper project's functionalities.
