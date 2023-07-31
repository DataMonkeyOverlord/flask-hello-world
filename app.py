import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://bh_123_user:9UbstWz5lrwnwNuF62Xr8qHD2jjHH0rj@dpg-cj232pc07spkp67l4cqg-a.oregon-postgres.render.com/bh_123")
    conn.close()
    return 'Database Connection Sucessful!'

@app.route('/db_create')
def make_db():
    conn = psycopg2.connect("postgres://bh_123_user:9UbstWz5lrwnwNuF62Xr8qHD2jjHH0rj@dpg-cj232pc07spkp67l4cqg-a.oregon-    postgres.render.com/bh_123")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
     ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Sucessfully Created!'


@app.route('/db_insert')
def insert_db():
    conn = psycopg2.connect("postgres://bh_123_user:9UbstWz5lrwnwNuF62Xr8qHD2jjHH0rj@dpg-cj232pc07spkp67l4cqg-a.oregon-    postgres.render.com/bh_123")
    cur = conn.cursor()
    cur.execute('''INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);'''
    conn.commit()
    conn.close()
    return 'Basketball Table Sucessfully Populated!'
                
                
@app.route('/db_select')
def select_db():
    conn = psycopg2.connect("postgres://bh_123_user:9UbstWz5lrwnwNuF62Xr8qHD2jjHH0rj@dpg-cj232pc07spkp67l4cqg-a.oregon-    postgres.render.com/bh_123")
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Basketball;'''
    records = cur.fetchall()             
    conn.close()
    response_string = ""
    response_string += '<table>'
        for player in records:
             response_string+= '<tr>'
             for info in player:
                response_string += "<td>{}</td>".format(info)
             response_string+="</tr>"
         response_string+="</table>"       
    return response_string     
                
                
@app.route('/db_drop')
def drop_db():
    conn = psycopg2.connect("postgres://bh_123_user:9UbstWz5lrwnwNuF62Xr8qHD2jjHH0rj@dpg-cj232pc07spkp67l4cqg-a.oregon-    postgres.render.com/bh_123")
    cur = conn.cursor()
    cur.execute('''DROP TABLE Basketball;'''       
    cur.commit()
    conn.close()  
    return "Basketball Table Sucessfully Dropped"                  
                

                



    

    



