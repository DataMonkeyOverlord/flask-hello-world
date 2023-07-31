import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://bh_123_user:9UbstWz5lrwnwNuF62Xr8qHD2jjHH0rj@dpg-cj232pc07spkp67l4cqg-a/bh_123")
    conn.close()
    return 'Database Connection Sucessful!'



