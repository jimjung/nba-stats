import sqlite3

def create_database():
    conn = sqlite3.connect('data/nba_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS teams
                 (name TEXT, record TEXT)''')
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('data/nba_data.db')
    c = conn.cursor()
    # Assuming data is a list of dictionaries
    data = [{'name': 'Lakers', 'record': '10-5'}, {'name': 'Warriors', 'record': '12-3'}]
    c.executemany('INSERT INTO teams VALUES (:name, :record)', data)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    insert_data() 