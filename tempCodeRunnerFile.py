import pandas as pd
import sqlite3

# Load data from Excel file
df = pd.read_excel('sports.xlsx')

# Store data in SQLite database
conn = sqlite3.connect('sports.db')
df.to_sql('sports', conn, if_exists='replace', index=False)

# Function to get recommendations based on age group
# def get_recommendations(age_group):
#     # Query to fetch sports preferences for the given age group
#     query = f"""
#         SELECT *
#         FROM sports
#         WHERE age_Group = '{age_group}'
#     """
#     # Execute the query
#     recommendations = pd.read_sql(query, conn)
#     return recommendations

def get_recommendations(age_group):
    # Query to fetch sports preferences for the given age group
    print("Column names in DataFrame:", df.columns)
    query = f"""
        SELECT *
        FROM sports
        WHERE [{age_group}] IS NOT NULL
    """
    # Execute the query
    recommendations = pd.read_sql(query, conn)
    return recommendations