


import pymysql

conn = pymysql.connect(host='localhost', user="root", password="", database="playersdb")

cursor = conn.cursor()

cursor.execute("delete from player where playerid = 'PL048'")

conn.commit()
conn.close()