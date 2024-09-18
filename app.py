from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
# Establish the MySQL connection
conn = pymysql.connect(
    host='localhost',
    user='kaka',
    password='password',
    db='myshop',
)

# Get a cursor object for executing SQL queries
cursor = conn.cursor()

@app.route('/submit', methods=['POST','GET'])
def submit_data():
    user_id = request.form['id']  # Fetch 'name' field from form
    name = request.form['name']  # Fetch 'name' field from form
    location = request.form['location']  # Fetch 'email' field from form

    # Insert into MySQL database
    sql = "INSERT INTO users (id,name, loaction) VALUES (%s, %s, %s)"
    cursor.execute(sql, (user_id,name, location))
    conn.commit()  # Commit the transaction to the database

    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)