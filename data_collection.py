```python
import sqlite3
from config import DATABASE_NAME

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        print(f'Successful connection with {DATABASE_NAME}')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def collect_data():
    conn = create_connection()
    cur = conn.cursor()

    business_plan_sections = ["Executive Summary", "Company Description", "Market Analysis", "Competitive Analysis", "Organization & Management", "Product Line or Services", "Marketing & Sales Strategy", "Funding Request", "Financial Projections", "Appendix"]

    user_data = {}

    for section in business_plan_sections:
        print(f"Please enter data for {section}: ")
        user_data[section] = input()

    for section, data in user_data.items():
        cur.execute(f"INSERT INTO business_plan(section, data) VALUES(?, ?)", (section, data))

    conn.commit()
    close_connection(conn)

if __name__ == "__main__":
    collect_data()
```