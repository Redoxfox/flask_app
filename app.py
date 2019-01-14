from flask import Flask
from models.conexion import db
app = Flask(__name__)

@app.route('/')
def hello_world():
    cursor = db().cursor()
    id = '4'
    sql = "INSERT INTO calendario (id) VALUES (%s);"
    cursor.execute(sql, (id))
    cursor.close()
    db().commit()
    return 'Hello from Flask!'

if __name__ == "__main__":
    app.run(debug = True, port = 8000)