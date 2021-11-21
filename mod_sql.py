import mysql.connector



def check_connect_mysql():
	print(" CHECK SQL  CONNECTION       : ",end='',flush=True)
	try:
		mydb = mysql.connector.connect(host="127.0.0.1",user="cicada3301",passwd="binpass",database="all_bin")
		mycursor = mydb.cursor()
		print("MYSQL CONNECTED OK ")
		time.sleep(2)
		#return mycursor
	except  Exception as e :
		#print("FIELED")
		print(" SQL ERROR CONNECTION        : "+str(e)+" ",end='',flush=True)
		# fix_mysql(str(e))
check_connect_mysql()