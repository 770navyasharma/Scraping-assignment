#importing all relevant libraries and methods for doing Scraping, handling URL's and establishing database connection to postgreSQL

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import psycopg2
from psycopg2 import sql

# Database connection details
db_params = {
    'dbname': 'nhl_data',
    'user': 'postgres',
    'password': 'kyamujhepyarhai',
    'host': 'localhost',
    'port': 5432
}

# Connection to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()
print("Connection Successful!")

# Creating the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS nhl_stats_search (
    id SERIAL PRIMARY KEY,
    team_name VARCHAR(255),
    year INT,
    wins INT,
    losses INT,
    ot_losses INT,
    win_percent FLOAT,
    goals_for INT,
    goals_against INT,
    goal_difference INT
);
"""
cursor.execute(create_table_query)
conn.commit()
print("Table created Successfully!")


def search_site(query):
    search_url = "https://www.scrapethissite.com/pages/forms/"
    params = {
        'q': query,
    }
    response = requests.get(search_url, params=params)
    response.raise_for_status()
    return response.text


# Function to insert data into the PostgreSQL database
def insert_data(team_name, year, wins, losses, ot_losses, win_percent, goals_for, goals_against, goal_difference):
    insert_query = sql.SQL("""
        INSERT INTO nhl_stats_search (
            team_name, year, wins, losses, ot_losses, win_percent, goals_for, goals_against, goal_difference
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """)
    cursor.execute(insert_query, (
        team_name, year, wins, losses, ot_losses, win_percent, goals_for, goals_against, goal_difference
    ))
    conn.commit()
    print("Data inserted Successfully!")
    
    
# Function to scrape data from a single page
'''
    Takes in the url of the page and returns the next directing
    element for getting the url for the next page
'''
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    
    #scraping the table on the page
    table = soup.find('table', {'class': 'table'})
    rows = table.find_all('tr')[1:]  # Skip the header row
    next_page_element = None
    for row in rows:
        cols = row.find_all('td')
        team_name = cols[0].text.strip()
        year = int(cols[1].text.strip())
        wins = int(cols[2].text.strip())
        losses = int(cols[3].text.strip())
        if(cols[4].text.strip()):
            ot_losses = int(cols[4].text.strip())
        else:
            ot_losses = None
        win_percent = float(cols[5].text.strip())
        goals_for = int(cols[6].text.strip())
        goals_against = int(cols[7].text.strip())
        goal_difference = int(cols[8].text.strip())
        # Insert the data into PostgreSQL
        insert_data(team_name, year, wins, losses, ot_losses, win_percent, goals_for, goals_against, goal_difference)
    next_page_element = soup.find('a', attrs={"aria-label": "Next"})
    return next_page_element
    


query = input("Enter team name : ")
query = query.split(' ')
elem = ""
for i in range(len(query)):
    if(i!=len(query)-1):
        elem = elem + query[i] + "+"
    else:
        elem = elem + query[i]

url = "https://www.scrapethissite.com/pages/forms/?page_num=1&q="+elem

# using url = "https://www.scrapethissite.com/pages/forms/?page_num=1" would give out all the entries in all the pages with the following code however the method implemented does it for user specified input team data entries only and saves them to postgres database.

next_page_element = scrape_page(url)
while True:
    if next_page_element:
        next_page_url = next_page_element.get('href')
        url = urljoin(url,next_page_url)
        next_page_element = scrape_page(url)
    else:
        break
    

