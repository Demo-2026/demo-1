import sqlite3
import os

def city_kpi(city: str):
    """
    Calculates KPI (Count and Average Spend) for a given city.
    Uses parameterized queries to prevent SQL injection.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, 'data', 'db', 'analytics.db')

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # SECURE: Using '?' handles escaping automatically
        query = "SELECT COUNT(*) as count, AVG(monthly_spend) as avg_spend FROM customers_raw WHERE city = ?"
        cursor.execute(query, (city,))
        result = cursor.fetchone()
        return result

if __name__ == "__main__":
    # Normal call
    print(f"Mumbai Stats (Count, Avg): {city_kpi('Mumbai')}")
    
    # Injection attempt call
    print(f"Injection Attempt Stats: {city_kpi(\"Mumbai' OR 1=1 --\")}")