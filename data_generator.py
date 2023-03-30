import psycopg2
import os
import dotenv

dotenv.load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST_EXTERNAL'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn


if __name__ == '__main__':
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS products")
            cur.execute("CREATE TABLE products (id SERIAL PRIMARY KEY , name varchar(255), category varchar(255))")

            cur.execute("INSERT INTO products (name, category) VALUES (%s, %s)", ('Lego Mindstorm', 'toys'))
            cur.execute("INSERT INTO products (name, category) VALUES (%s, %s)", ('Lego City', 'toys'))
            cur.execute("INSERT INTO products (name, category) VALUES (%s, %s)", ('Leather ball', 'sport'))

            conn.commit()
