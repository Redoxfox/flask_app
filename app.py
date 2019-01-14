#-----------------------------------------------------------------------------------------------------------------------
#Datos de configuracion
#-----------------------------------------------------------------------------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors
from lib.Bbinaria import binaria
from lib.Oquicksort import quicksort
from lib.calendario import fechas_liga

# Connect to the database
"""connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='perfume',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)"""

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
    sql = "SELECT * FROM liga " #
    cursor.execute(sql)
    result = cursor.fetchall()
    resultado = {}
    cont = 0
    for rows in result:
        idlig = rows["id"]
        nombre = rows["nombre"]
        pais = rows["pais"]
        continente = rows["continente"]
        url = "http://redoxfox1.pythonanywhere.com/clasificacion/" + str(idlig) + "/"
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
#-----------------------------------------------------------------------------------------------------------------------
#Datos clasificacion
#-----------------------------------------------------------------------------------------------------------------------
@app.route('/clasificacion/<id>/', methods=['POST', 'GET'])
def liga(id):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM calendario WHERE id_liga=%s and estado='PENDIENTE'", str(id))
    result = cursor.fetchall()
    resultado = {}
    cont = 0
    Jornada = 1
    for rows in result:
        idlig = rows["id_liga"]
        nrofecha = rows["nro_fecha"]
        idp = rows["id"]
        ps = rows["equipo_1"]
        ps2 = rows["equipo_2"]
        gol_eq1 = rows["gol_eq1"]
        gol_eq2 = rows["gol_eq2"]
        cursor.execute("SELECT nombre FROM equipos WHERE id=%s", ps)
        nom_eq = cursor.fetchone()
        equipo_1 = nom_eq['nombre']
        cursor.execute("SELECT nombre FROM equipos WHERE id=%s", ps2)
        nom_eq2 = cursor.fetchone()
        equipo_2 = nom_eq2['nombre']
        url = "http://localhost:8000/resultado/" + str(idp) + "/" + str(idlig) + "/" + str(ps) + "/" + str(ps2)+ "/"
        urlrev = "http://localhost:8000/"
        if Jornada != nrofecha:
           Jornada = nrofecha
           cambio = 'true'
           idj = "J" + str(Jornada) + "-P" + str(idp)
           resultado[cont] = (equipo_1, gol_eq1, equipo_2, gol_eq2, url, idj, cambio)
        else:
           idj = "J" + str(Jornada) + "-P" + str(idp)
           cambio = 'false'
           resultado[cont] = (equipo_1, gol_eq1, equipo_2, gol_eq2, url, idj, cambio)

        cont = cont + 1

    return render_template('clasificacion.html', result=resultado, nombre=id, liga = 'española', url = urlrev )
"""if __name__ == "__main__":
    app.run(debug = True, port = 8000)"""