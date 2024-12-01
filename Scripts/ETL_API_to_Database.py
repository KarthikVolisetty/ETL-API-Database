# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:33:55 2024

@author: karth
"""

import requests
import psycopg2

# ------------------------------------------- Stage - 1: Extract ------------------------------------------------ #
# This section is responsible for extracting cryptocurrency price data from the CoinGecko API.

# Define the API endpoint URL for fetching cryptocurrency data.
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

# Make a GET request to the API and store the response.
response = requests.get(url)

# Parse the JSON response into a Python dictionary.
data = response.json()

# Print the extracted data to verify the response structure.
print("Extracted Data:", data)


# ------------------------------------------- Stage - 2: Transform ---------------------------------------------- #
# This section transforms the extracted data into a tabular format suitable for database insertion.

# Initialize an empty list to store the transformed data.
tabular_data = []

# Iterate through the key-value pairs in the extracted data.
print("Data Items:", data.items())
for crypto, values in data.items():
    # For each cryptocurrency, iterate through its currency values.
    for currency, value in values.items():
        # Append the data as a tuple (crypto name, currency type, value) to the list.
        tabular_data.append((crypto, currency, value))

# Print the transformed data to verify the structure.
print("Tabular Data:", tabular_data)


# ------------------------------------------- Stage - 3: Load ---------------------------------------------------- #
# This section loads the transformed data into a PostgreSQL database.

# Database configuration parameters
db_config = {
    'host': 'localhost',
    'database': 'Practice',
    'user': 'postgres',
    'password': 'Karthik@1261'
}

# Establish a connection to the PostgreSQL database.
conn = psycopg2.connect(**db_config)
cur = conn.cursor()
print("Database Connection Successful")

# Define the table name where data will be inserted.
table_name = 'CRYPTO'

# Extract the first item from the API response for dynamic table creation.
extract_data = next(iter(data.items()))
crypto_data = extract_data[0]  # The cryptocurrency name
print("Cryptocurrency:", crypto_data)

column_data = extract_data[1]  # Currency and its corresponding value
print("Currency Data:", column_data.items())

# Dynamically create column definitions based on the keys in the API response.
columns_create = [f"{key} NUMERIC" for key in column_data.keys()]
column_create_definition = ', '.join(columns_create)
print("Column Definitions:", column_create_definition)

# Construct the SQL query to create the table if it does not exist.
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_create_definition});"
cur.execute(create_table_query)
conn.commit()
print(f"Table '{table_name}' created successfully")

# Prepare the column names and their corresponding values for insertion.
columns = [f"{key}" for key in column_data.keys()]
column_definition = ', '.join(columns)
values = [f"{value}" for value in column_data.values()]
value_definition = ', '.join(values)

# Construct the SQL query to insert data into the table.
insert_query = f"INSERT INTO {table_name} ({column_definition}) VALUES ({value_definition});"
print("Insert Query:", insert_query)

# Execute the insertion query and commit the changes to the database.
cur.execute(insert_query)
conn.commit()
print("Data loaded successfully")

# Close the database cursor and connection.
cur.close()
conn.close()


