

import pymysql

conn = pymysql.connect(host='localhost', user="root", password="", database="playersdb")

cursor = conn.cursor()

cursor.execute("update player set playername = 'Pusarla Venkata Sindhu' where playerid = 'PL052'")

conn.commit()
conn.close()