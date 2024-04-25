
import pymysql


conn = pymysql.connect(host='localhost', user='root', password='')

cursor = conn.cursor()
cursor.execute("create database playersdb")

conn.close()
