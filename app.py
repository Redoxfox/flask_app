#-----------------------------------------------------------------------------------------------------------------------
#Datos de configuracion
#-----------------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors
from lib.Bbinaria import binaria
from lib.Oquicksort import quicksort
from lib.calendario import fechas_liga

# Connect to the database
connection = pymysql.connect(host='redoxfox1.mysql.pythonanywhere-services.com',
                             user='redoxfox1',
                             password='Fox841204',
                             db='redoxfox1$perfume',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
app = Flask(__name__)

#-----------------------------------------------------------------------------------------------------------------------
#Inicio aplicacion
#-----------------------------------------------------------------------------------------------------------------------
@app.route("/")
def home():
    cursor=connection.cursor()
    # Read a single record
    sql = "SELECT * FROM liga " 
    cursor.execute(sql)
    result = cursor.fetchall()
    resultado = {}
    cont = 0
    for rows in result:
        idlig = rows["id"]
        nombre = rows["nombre"]
        pais = rows["pais"]
        continente = rows["continente"]
        url = "http://localhost:8000/clasificacion/" + str(idlig) + "/"
        resultado[cont] = (idlig,  nombre, pais, continente, url)
        cont = cont + 1
    sql1 = " select id from liga;"
    cursor.execute(sql1)
    ligas = cursor.fetchall()
    ligas_reg = []
    jornadas = []
    for rows in ligas:
        nro_liga = rows["id"]
        ligas_reg.append(nro_liga)
    liga_ext = len(ligas) + 1
    ligas_reg.append(liga_ext)
    for i in range(1, 45):
        jornadas.append(i)

    return render_template('home.html', result=resultado, ligas_reg = ligas_reg, jornadas = jornadas )
    