import requests
import psycopg2
from psycopg2 import sql


# Function to fetch data for a specific year
def fetch_data_for_year(year):
    url = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true'
    params = {'year': year}
    response = requests.get(url, params=params)
    return response.json()

# Function to insert data into PostgreSQL
def insert_data_to_postgres(data):
    conn = psycopg2.connect(
        database = "MovieLIS", user = "postgres",password = "kyamujhepyarhai", host = "127.0.0.1", port = "5432"
    )
    cursor = conn.cursor()
    print("Connection Successful!")
    create_table_query = """create table if not exists films(title varchar(60),nominations integer,awards integer,year integer, best_picture varchar(10));"""
    cursor.execute(create_table_query)
    conn.commit()
    print("Table created Successfully!")
    insert_query = sql.SQL("""
        INSERT INTO films (title, nominations, awards, year, best_picture)
        VALUES (%s, %s, %s, %s, %s)
    """)
    
    for film in data:
        if 'best_picture' in film.keys():
            fb = film['best_picture']
        else:
            fb = None
        data = (film['title'],film['nominations'],film['awards'],film['year'],fb)
        cursor.execute(insert_query, data)

    conn.commit()
    cursor.close()
    conn.close()

# Main scraping logic
years = [2010, 2011, 2012, 2013, 2014, 2015]
for year in years:
    data = fetch_data_for_year(year)
    print(data)
    insert_data_to_postgres(data)
    print(f"Data for {year} inserted successfully.")
