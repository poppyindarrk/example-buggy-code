import sqlite3

def query_database(db_path, query):
    # Bug: Not using context managers can lead to connections not being closed
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    # Missing cursor and connection close statements
    return results
