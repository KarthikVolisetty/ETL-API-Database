ETL: Cryptocurrency Data from CoinGecko API to PostgreSQL

**README.md**

# ETL: Cryptocurrency Data from CoinGecko API to PostgreSQL

## Description
This ETL (Extract, Transform, Load) process fetches real-time cryptocurrency price data from the CoinGecko API, processes it into a tabular format, and loads it into a PostgreSQL database. The program dynamically handles the data structure returned by the API and ensures the database table is created accordingly.

## Key Features
- **Data Source**: CoinGecko API (`https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd`).
- **Transformations**:
  - Extracts cryptocurrency prices and associated currencies.
  - Converts the data into a structured tabular format (cryptocurrency name, currency type, price).
- **Database**: PostgreSQL.
- **Dynamic Table Creation**: Automatically defines columns based on the API response.

## Prerequisites
1. **Python Packages**:
   - Install the required libraries:
     ```bash
     pip install requests psycopg2
     ```
2. **PostgreSQL**:
   - Ensure PostgreSQL is installed and running.
   - Create a database named `Practice` (or modify the script to match your setup).

## Files
- `ETL_API_to_Database.py`: Python script to perform the ETL process.

## How to Run
1. Clone the repository or save the script to your local machine.
2. Update the `db_config` dictionary in the script with your PostgreSQL credentials:
   ```python
   db_config = {
       'host': 'localhost',
       'database': 'Practice',
       'user': 'postgres',
       'password': 'YourPassword'
   }
   ```
3. Run the script:
   ```bash
   python ETL_API_to_Database.py
   ```
4. Verify the table and data in the PostgreSQL database:
   - The table name will be `CRYPTO`.
   - The table will include columns for the currencies and their respective prices.

## Output
- The script creates a table named `CRYPTO` in the PostgreSQL database.
- Inserts real-time cryptocurrency price data (e.g., Bitcoin in USD) into the table.
