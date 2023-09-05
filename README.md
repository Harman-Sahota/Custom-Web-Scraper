# Custom Web Scraper Application

## Table of Contents

1. [Overview](#Overview)
2. [Tech Stack](#Tech-Stack)
3. [Installation](#Installation)
    - [Python](##Python)
    - [Required Packages](##Required-Packages)
    - [MySQL Workbench](##Mysql-Workbench)
4. [Database Setup](#Database-Setup)
    - [Configuring the Database](##Configuring-The-Database)
5. [Running the Application](#Running-The-Application)
6. [Usage](#Usage)
    - [Landing Page](##Landing-Page)
    - [Website List Page](##Website-List-Page)
    - [Keyword Search Page](##Keyword-Search-Page)
    - [Login Feature](##Login-Feature)
7. [API Endpoints](#API-Endpoints)
   - [Partial API Integration](##Partial-API-Integration)
8. [Partial API Integration](#partial-api-integration)
10. [Conclusion](#conclusion)


# Overview

The **Custom Web Scraper Application** is a versatile web scraping and data extraction tool built on the Django web framework. It empowers users to extract valuable information from websites, categorize results, and perform keyword-based searches with ease. This customizable and user-friendly application serves as a foundation for web scraping projects and provides essential features for data retrieval and analysis.

# Tech Stack

Note: This is a high level overview of the technologies used, and there might be some packages missing. 

| Technology         | Description                                      |
|--------------------|--------------------------------------------------|
| Django             | Web framework for building web applications      |
| Python             | Programming language for backend development    |
| HTML/CSS           | Frontend markup and styling                     |
| JavaScript         | Frontend and dynamic behavior                   |
| Bootstrap          | Frontend framework for responsive design        |
| MySQL              | Relational database management system           |
| Requests           | Python library for making HTTP requests         |
| BeautifulSoup      | Python library for web scraping                 |
| Axios              | JavaScript library for making HTTP requests     |
| REST Framework     | Toolkit for building Web APIs                    |
| jQuery             | JavaScript library for DOM manipulation         |
| Git                | Version control system for code management      |


## Key Features

1. **Website List Management:** Users can add and categorize websites in the application's database. Each website is associated with a category, making it easy to organize and filter data.

2. **Keyword-Based Search:** The application allows users to perform keyword-based searches on the list of websites. It retrieves relevant information from websites based on user-defined keywords, streamlining data retrieval.

3. **Dynamic Results:** Search results are displayed dynamically, providing real-time feedback to users. Both API data and scraped data are presented in a user-friendly format for quick analysis.

4. **API Integration (Partial):** While API integration is partially complete, the application supports identifying and separating API URLs from regular URLs. Further development is required to fully implement API data retrieval and integration.

5. **Database Integration:** The application employs a MySQL database to store website information and search results. Users can set up the database easily using provided SQL scripts.

6. **User-Friendly Interface:** The user interface is designed with user experience in mind. Bootstrap is used to create a responsive and visually appealing design.

7. **Customization:** Developers can customize and extend the application to meet specific scraping requirements. It serves as a foundation for more advanced web scraping projects.

8. **Documentation:** The project includes comprehensive documentation to guide users through installation, setup, and usage. Troubleshooting and configuration instructions are also provided.

**Please Note:** The login feature is not yet implemented in the current version of the application.

The Custom Web Scraper Application is a valuable tool for researchers, data analysts, and web scraping enthusiasts who need a robust and adaptable solution for extracting data from websites. It simplifies the process of web scraping and empowers users to access and analyze information efficiently.

Whether you're conducting market research, gathering insights, or conducting data-driven studies, the Custom Web Scraper Application offers the flexibility and functionality needed to achieve your web scraping goals.

# Installation

##  Python

Before you begin, make sure you have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/).

## Required Packages 

The application relies on several Python packages for its functionality. To install these packages, open a terminal or command prompt, navigate to your project directory, and run the following command:

```bash
pip install -r requirements.txt
```

The 'requirements.txt' file contains a list of all required packages, including Django and various libraries used by the application.

## Mysql Workbench 

To set up the database for the application, you'll need MySQL Workbench. If you haven't already installed it, you can download MySQL Workbench from the official website: [MySQL Workbench Downloads](https://dev.mysql.com/downloads/workbench/)

# Database Setup

- Launch MySQL Workbench and connect to your MySQL server.
- Open the [scraping.sql](https://github.com/Harman-Sahota/Custom-Web-Scraper/blob/main/scraping_project/scraping.sql) file provided with the application.
- Execute the SQL script in scraping.sql to set up the database schema and tables required for the application.

## Configuring the Database

- After executing the SQL script, you should have the necessary database schema and tables created. Make sure to note the database credentials, such as the username, password, and database name, as you'll need these later.
- Next, you need to configure the database settings in the Django project. Open the settings.py file located in the scraping_project directory.
- Locate the following section in the [settings.py](https://github.com/Harman-Sahota/Custom-Web-Scraper/blob/main/scraping_project/scraping_project/settings.py) file and update it with your database configuration:
  
```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host', # Typically 'localhost' for local development
        'PORT': 'your_database_port', # Default MySQL port is 3306
    }
}
```

Replace 'your_database_name', 'your_database_user', 'your_database_password', 'your_database_host', and 'your_database_port' with your actual database credentials.

# Running the Application

- Once the database is set up and the required packages are installed, you can run the application using the following command in the terminal with the path inside the 'scraping_project' folder: 

```bash
python manage.py runserver
```

- Open a web browser and navigate to http://localhost:8000/ to access the application.

# Usage

## Landing Page

The landing page (landing_page.html)  serves as the entry point for the application. Here, users can find information about the Custom Web Scraper and access the login functionality.

Link to the landing page - 'http://localhost:8000/'  or 'http://127.0.0.1:8000'.

## Website List Page

The "Add Website" page (WebsiteList.html) allows users to add websites to the database. Users can enter the website's URL and select a category from the dropdown.

Link to the  page - 'http://localhost:8000/WebsiteList'  or 'http://127.0.0.1:8000/WebsiteList'.

## Keyword Search Page

The "Search Websites" page (KeywordSearch.html) enables users to perform keyword-based searches on the list of websites. Users can enter a keyword and select a category to filter results.

Link to the  page - 'http://localhost:8000/KeywordSearch'  or 'http://127.0.0.1:8000/KeywordSearch'.

## Login Feature

The login feature allows authorized users to access the application's functionality securely and personalizer a users experience. However, please note that the login feature is currently under development and may not be fully functional in the current version of the application.

# API Endpoints

The Custom Web Scraper Application provides API endpoints for performing keyword-based searches and retrieving data from websites. These endpoints can be accessed programmatically to integrate the application with external systems.

## Partial API Integration
The API integration feature of the application is currently in progress. As of the current version, the application can identify API URLs and separate them from regular URLs. Further development is required to fully implement API data retrieval and integration.


# Conclusion

The Custom Web Scraper Application offers a powerful and customizable solution for web scraping and data extraction. With its user-friendly interface, database integration, and API support, it simplifies the process of accessing and analyzing data from websites. Developers can extend and customize the application to meet specific scraping requirements, making it a valuable tool for various use cases.


Please note that the login feature is mentioned as currently under development in this documentation. You can update this section with details once the feature is fully implemented.

** Last Updated - Sep 5, 5:30 pm EST

  
