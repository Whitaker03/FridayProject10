import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('feedback.db')

# Load data from the feedback table, selecting the 'comment' column
reviews_df = pd.read_sql_query("SELECT id, comment FROM feedback", conn)

# Inspect the DataFrame
print(reviews_df.head())

# Close the database connection
conn.close()
