import psycopg2

conn = psycopg2.connect("dbname = postgres user = postgres password = 9817")

cursor = conn.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS test;
''')

cursor.execute('''
    CREATE TABLE test (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
    );
''')

cursor.execute('INSERT INTO test (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO test (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
    'id': 2,
    'completed': False
}

cursor.execute('SELECT * from test')
result = cursor.fetchall()
print(result)


cursor.execute(SQL, data)
conn.commit()

cursor.close()

