import pandas as pd
import sqlite3
import os

def load_data(): #to load data
    # Define paths relative to this script (src/ -> demo-1/)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'raw', 'customers_raw.csv')
    db_dir = os.path.join(base_dir, 'data', 'db')
    db_path = os.path.join(db_dir, 'analytics.db')

    # Ensure DB directory exists
    os.makedirs(db_dir, exist_ok=True)

    # Load CSV and write to SQLite
    df = pd.read_csv(csv_path)
    with sqlite3.connect(db_path) as conn:
        df.to_sql('customers_raw', conn, if_exists='replace', index=False)
    print(f"Successfully loaded {len(df)} rows into {db_path}")

if __name__ == "__main__":
    load_data()