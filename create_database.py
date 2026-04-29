"""
Caveman Mode: Create SQLite database from clean JSON data
"""
import json
import sqlite3

def create_sqlite_database():
    """Convert problems.json to SQLite database"""

    # Load clean data
    with open('problems.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)

    # Create SQLite database
    conn = sqlite3.connect('dsa_sheet.db')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problems (
            id INTEGER PRIMARY KEY,
            topic TEXT,
            subtopic TEXT,
            name TEXT,
            link TEXT,
            status TEXT DEFAULT 'not_started'
        )
    ''')

    # Clear existing data
    cursor.execute('DELETE FROM problems')

    # Insert data
    for problem in problems:
        cursor.execute('''
            INSERT INTO problems (id, topic, subtopic, name, link, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            problem['id'],
            problem['topic'],
            problem['subtopic'],
            problem['name'],
            problem['link'],
            problem['status']
        ))

    # Commit and close
    conn.commit()
    conn.close()

    print(f"Created SQLite database with {len(problems)} problems")
    print(f"Database file: dsa_sheet.db")

    # Verify the data
    conn = sqlite3.connect('dsa_sheet.db')
    cursor = conn.cursor()

    # Show sample data
    cursor.execute('SELECT * FROM problems LIMIT 3')
    sample_data = cursor.fetchall()

    print(f"\nSample data from database:")
    for row in sample_data:
        print(f"  ID: {row[0]}, Topic: {row[1]}, Subtopic: {row[2]}, Name: {row[3]}")

    # Show statistics
    cursor.execute('SELECT topic, COUNT(*) FROM problems GROUP BY topic ORDER BY COUNT(*) DESC')
    topic_stats = cursor.fetchall()

    print(f"\nTopic distribution:")
    for topic, count in topic_stats:
        print(f"  {topic}: {count}")

    conn.close()

if __name__ == "__main__":
    create_sqlite_database()