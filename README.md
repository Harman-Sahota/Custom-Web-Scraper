# Custom Web Scraper Application

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
    - [Python](#python)
    - [Required Packages](#required-packages)
    - [MySQL Workbench](#mysql-workbench)
3. [Database Setup](#database-setup)
    - [Configuring the Database](#configuring-the-database)
4. [Running the Application](#running-the-application)
5. [Usage](#usage)
    - [Landing Page](#landing-page)
    - [Website List Page](#website-list-page)
    - [Keyword Search Page](#keyword-search-page)
    - [Login Feature](#login-feature)
6. [API Endpoints](#api-endpoints)
7. [Partial API Integration](#partial-api-integration)
8. [Troubleshooting](#troubleshooting)
9. [Conclusion](#conclusion)


# 1. Overview

The **Custom Web Scraper Application** is a versatile web scraping and data extraction tool built on the Django web framework. It empowers users to extract valuable information from websites, categorize results, and perform keyword-based searches with ease. This customizable and user-friendly application serves as a foundation for web scraping projects and provides essential features for data retrieval and analysis.

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
