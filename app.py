# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import pymysql.cursors
app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='redoxfox1.mysql.pythonanywhere-services.com',
                             user='redoxfox1',
                             password='Fox841204',
                             db='redoxfox1$perfume',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

if __name__ == "__main__":
    app.run(debug = True, port = 8000)