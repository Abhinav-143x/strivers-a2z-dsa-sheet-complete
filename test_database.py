"""
Caveman Mode: Simple database queries to demonstrate usability
"""
import sqlite3

def run_caveman_queries():
    """Run simple queries to show data is usable"""

    conn = sqlite3.connect('dsa_sheet.db')
    cursor = conn.cursor()

    print("=== CAVEMAN MODE DATABASE QUERIES ===\n")

    # Query 1: Get all problems
    print("1. Total problems in database:")
    cursor.execute('SELECT COUNT(*) FROM problems')
    total = cursor.fetchone()[0]
    print(f"   {total} problems\n")

    # Query 2: Get problems by topic
    print("2. Problems by topic:")
    cursor.execute('SELECT topic, COUNT(*) FROM problems GROUP BY topic ORDER BY COUNT(*) DESC LIMIT 5')
    for row in cursor.fetchall():
        print(f"   {row[0]}: {row[1]}")
    print()

    # Query 3: Get easy problems
    print("3. Easy problems:")
    cursor.execute('SELECT id, name FROM problems WHERE subtopic = "Easy" LIMIT 5')
    for row in cursor.fetchall():
        print(f"   {row[0]}. {row[1]}")
    print()

    # Query 4: Get problems with links
    print("4. Problems with practice links:")
    cursor.execute('SELECT id, name, link FROM problems WHERE link != "" LIMIT 3')
    for row in cursor.fetchall():
        print(f"   {row[0]}. {row[1]}")
        print(f"      Link: {row[2]}")
    print()

    # Query 5: Update a problem status
    print("5. Update problem status (Caveman Mode test):")
    cursor.execute('UPDATE problems SET status = "completed" WHERE id = 1')
    conn.commit()
    print("   Marked problem #1 as completed")

    cursor.execute('SELECT id, name, status FROM problems WHERE id = 1')
    row = cursor.fetchone()
    print(f"   {row[0]}. {row[1]} - Status: {row[2]}")
    print()

    # Query 6: Get completion stats
    print("6. Completion status:")
    cursor.execute('SELECT status, COUNT(*) FROM problems GROUP BY status')
    for row in cursor.fetchall():
        print(f"   {row[0]}: {row[1]}")
    print()

    conn.close()
    print("=== CAVEMAN MODE COMPLETE ===")
    print("Data is usable. App can now be useful.")

if __name__ == "__main__":
    run_caveman_queries()