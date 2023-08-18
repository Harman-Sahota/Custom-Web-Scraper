#  Web Scraper Application

## Overview

The Custom Web Scraper Application is a Django-based tool designed to perform keyword searches on a predefined list of websites and store the search results in a CSV file. This application serves as a basic web scraping utility that can be extended and customized for various use cases.

## Setup and Usage

### Installation

1. Install the required packages using the following command:

```bash
pip install django djangorestframework beautifulsoup4 requests
```

2. Clone or download this repository to your local machine.

### Configuration

1. Define the keywords you want to search for in the `keywords.csv` file. Each keyword should be on a separate line.

2. Specify the URLs of the websites you want to search within the `websites.csv` file. Each URL should be on a separate line.

### Running the Application

1. Open a terminal window and navigate to the project directory.

2. Start the Django development server:

```bash
python manage.py runserver
```

3. Access the application by opening a web browser and navigating to `http://localhost:8000/search/`.

### API Endpoint

* `GET /search/`: Retrieves and displays the search results.

## Code Structure

* `views.py`: Contains the `SearchList` class, which performs keyword searches and saves results.
* `models.py`: Defines the `Search` model used for storing search results.
* `serializers.py`: Provides the `SearchSerializer` for serializing search results.

## Usage

1. The application first loads keywords and websites from the respective CSV files.

2. It then performs searches for each keyword on all websites.

3. For each website and keyword combination, the application scrapes the website content and checks for the presence of the keyword.

4. The search results, including the website URL, keyword, whether the keyword was found, and relevant information, are saved to the `search_results.csv` file.

## Notes and Considerations

* Proper error handling is implemented for HTTP requests and HTML parsing to ensure stability.
* The application adheres to the Django REST Framework's `ListCreateAPIView` pattern.
* In a production environment, ensure proper separation of concerns between frontend and backend components.

