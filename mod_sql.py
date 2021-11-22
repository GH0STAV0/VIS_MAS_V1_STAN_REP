import mysql.connector

import time ,os
from datetime import datetime







bot_name='bot_tow'
mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")

# last_bin="50000000"

today_date = datetime.today().strftime('%d-%m-%Y')


def check_if_exist():

	print(" CHECK THE FILE  LAST_BIN IF EXIST  : ",end='',flush=True)
	PATH = './last_bin'
	if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
	    print("FILE EXIST : )")
	else:
	    print("MISSING FILE !!!")
	    open("last_bin", 'w').close()
	    creat_last_bin()






def insert_to_db():

	
	mycursor = mydb.cursor()

	sql = "INSERT INTO last_bin_sql (bot_name, last_bin,last_ssen) VALUES (%s, %s, %s)"
	val = ("bot_tow", "50000000","12-11-2021")
	mycursor.execute(sql, val)
	time.sleep(2)

	mydb.commit()


def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
	except  Exception as e :
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)


def update_to_db(bin0):
	check_connect_mysql()
	print(" UPDATE_SQL BIN [ "+bin0+" ] : ",end='',flush=True)

	
	mycursor = mydb.cursor()
	
	input=(bin0,today_date,bot_name)
	sql = "UPDATE last_bin_sql SET last_bin = %s , last_ssen= %s  WHERE bot_name = %s"
	mycursor.execute(sql,input)
	mydb.commit()
	print("[ SUCCED ] ")

def creat_last_bin():
	# print(" CREAT THE FILE LAST_BIN  : ",end='',flush=True)
	bina=get_value_last_bin()
	print("[ "+bina+" ]")
	with open('last_bin', "w") as myfile:
		myfile.write(bina)







def get_value_last_bin():

	print(" SEARCH_SQL LAST BIN OF [ "+bot_name+" ] : ",end='',flush=True)
	mycursor = mydb.cursor()
	sql = "SELECT * FROM last_bin_sql WHERE bot_name = %s"
	mycursor.execute(sql,(bot_name,))
	record = mycursor.fetchall()
	for row in record:
		sql_last_bin=row[2]
		# print(row[2])
	return sql_last_bin










# update_to_db(last_bin)
# insert_to_db()



# password wifi 36038860

# host remotemysql.com:3306

# user f6V3kVwxvH

# database f6V3kVwxvH

# pass sOVnW1130i
# check_connect_mysql()
# get_value_last_bin(bot_name)
check_if_exist()
# creat_last_bin()