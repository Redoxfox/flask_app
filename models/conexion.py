def db():
    import pymysql.cursors   
    connection = pymysql.connect(host='redoxfox1.mysql.pythonanywhere-services.com',
                             user='redoxfox1',
                             password='Fox841204',
                             db='redoxfox1$perfume',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection 
