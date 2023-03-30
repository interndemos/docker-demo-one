from dotenv import load_dotenv
import os
import flask
import psycopg2

# to run the app:
# python3 -m flask --app webapp run --debug -p 8888 -h 0.0.0.0

app = flask.Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(host=os.getenv('POSTGRES_HOST_EXTERNAL'),
                            database=os.getenv('POSTGRES_DB'),
                            user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'))

    with conn.cursor() as cur:
        cur.execute('SELECT * FROM products')
        rows = cur.fetchall()

    return flask.render_template('products.html', products=rows)

if __name__ == '__main__':
    load_dotenv()

    app.run(debug=True, port=8888, host='0.0.0.0')