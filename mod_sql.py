import mysql.connector

import time 
from datetime import datetime

bot_name='bot_tow'

last_bin="50000000"

today_date = datetime.today().strftime('%d-%m-%Y')


def insert_to_db():

	mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
	mycursor = mydb.cursor()

	sql = "INSERT INTO last_bin_sql (bot_name, last_bin,last_ssen) VALUES (%s, %s, %s)"
	val = ("bot_tow", "50000000","12-11-2021")
	mycursor.execute(sql, val)
	time.sleep(2)

	mydb.commit()


def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
		# time.sleep(2)
		#return mycursor
	except  Exception as e :
		#print("FIELED")
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)
		# fix_mysql(str(e))


def update_to_db(bin0,bot_name):

	mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
	mycursor = mydb.cursor()
	# sql = "UPDATE last_bin_sql SET last_bin = "+bin+", WHERE bot_name = '"+bot_name+"'"
	input=(bin0,today_date,bot_name)
	sql = "UPDATE last_bin_sql SET last_bin = %s , last_ssen= %s  WHERE bot_name = %s"

	# sql = "INSERT INTO last_bin_sql (bot_name, last_bin,last_ssen) VALUES (%s, %s, %s)"
	# val = ("bot_tow", "50000000","12-11-2021")
	mycursor.execute(sql,input)
	# time.sleep(2)
	mydb.commit()
	print("MYSQL updated OK ")










check_connect_mysql()

update_to_db(last_bin,bot_name)
# insert_to_db()



# password wifi 36038860

# host remotemysql.com:3306

# user f6V3kVwxvH

# database f6V3kVwxvH

# pass sOVnW1130i
