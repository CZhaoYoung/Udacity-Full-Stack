import psycopg2

conn = psycopg2.connect("dbname = testdb")

cursor = conn.cursor()

cursor.excute('''
    CREATE TABLE test (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
    );
''')

conn.commit()

cursor.close()

