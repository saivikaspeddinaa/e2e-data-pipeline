import psycopg2

def load_data(data):
    conn = psycopg2.connect(
        dbname="etl_db",
        user="postgres",
        password="Light@10",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    for row in data:
        cur.execute(
            "INSERT INTO posts (id, title) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING;",
            row
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded successfully!")