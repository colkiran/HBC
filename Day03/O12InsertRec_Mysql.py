
import pymysql

FL = open("Players.txt", 'r')

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb")

cursor = conn.cursor()

for line in FL.readlines():
    cursor.execute(line)

conn.commit()

FL.close()
conn.close()

