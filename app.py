import time

from dotenv import load_dotenv
import os
import flask
import psycopg2
from data_generator import generate_data

app = flask.Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(host=os.getenv('POSTGRES_HOST'),
                            database=os.getenv('POSTGRES_DB'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'))

    with conn.cursor() as cur:
        cur.execute('SELECT name, category FROM products')
        rows = cur.fetchall()

    return flask.render_template('products.html', products=rows)

if __name__ == '__main__':
    load_dotenv()

    retries = 0
    while retries < 10:
        try:
            generate_data()
            break
        except:
            time.sleep(1)

    app.run(debug=True, port=8888, host='0.0.0.0')