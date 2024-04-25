
import pymysql
from prettytable import PrettyTable, from_db_cursor

conn = pymysql.connect(host='localhost', user="root", password="", database="playersdb")

cursor = conn.cursor()

cursor.execute("select * from player")

# for row in cursor.fetchall():
#     print(row)

prtTbl = from_db_cursor(cursor)

print(prtTbl)

conn.close()
