# Web Scraping Projects
## Overview
### This repository contains two web scraping projects:

- Hockey Team Statistics Scraper: Scrapes NHL team statistics and stores the data in a PostgreSQL database.
- Movie Information Scraper: Scrapes movie information for specific years and stores the data in a PostgreSQL database.
### Prerequisites
To run these projects, you need the following installed on your machine:

- Python 3
- PostgreSQL
- Required Python libraries: requests, beautifulsoup4, psycopg2, urllib
#### Install the required Python libraries using pip:
* pip install requests beautifulsoup4 psycopg2
## Project 1: Hockey Team Statistics Scraper
### Description
#### The sraper.py script scrapes NHL team statistics from https://www.scrapethissite.com/pages/forms/ and saves the data to a PostgreSQL database.

Make sure to update the database connection details in scraper.py and you should have a database named nhl_data.

Run the script:
- python scraper.py
Enter the team name you want to search for when prompted.
### Code Explanation
- Import Libraries: The script imports necessary libraries for scraping and database operations.
- Database Connection: Establishes a connection to the PostgreSQL database and creates a table if it doesn't exist.
- Search Function: Constructs a search URL based on user input and fetches the search results.
- Insert Data Function: Inserts scraped data into the PostgreSQL database.
- Scrape Page Function: Scrapes data from a single page and follows pagination links to scrape additional pages.
## Project 2: Movie Information Scraper
### Description
#### The script scrapes movie information for the years 2010 to 2015 from https://www.scrapethissite.com/pages/ajax-javascript/#2015 and saves the data to a PostgreSQL database.

Make sure to update the database connection details in scraper.py and you should have a database named MovieLIS.

Run the script:
- python scraper.py
### Code Explanation
- Import Libraries: The script imports necessary libraries for fetching data and database operations.
- Fetch Data Function: Fetches movie data for a specific year using AJAX requests.
- Insert Data Function: Inserts the fetched movie data into the PostgreSQL database.
- Main Scraping Logic: Iterates through the specified years, fetches data for each year, and inserts it into the database.
### Notes
- Ensure that your PostgreSQL server is running and accessible.
- Update the database connection details as per your local setup.
- The scripts handle pagination, searching and AJAX requests to scrape dynamic content.
