#!python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Jim'
app.config['MYSQL_PASSWORD'] = 'Chance.21'
app.config['MYSQL_DB'] = 'firstschema'
 
mysql = MySQL(app)
Flask MySQL Step 2
@app.route("/")

def index():
    return render_template('index.html')
    
def main():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True, port=80)