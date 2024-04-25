
import pymysql

conn = pymysql.connect(host='localhost', user='root', password="", database="playersdb")

cursor = conn.cursor()

query = """
create table player (
playerid varchar(5) Primary Key, 
playername varchar(50) not null,
sport varchar(30) not null,
achievement varchar(30) not null
)
"""
cursor.execute(query)

conn.commit()
conn.close()
