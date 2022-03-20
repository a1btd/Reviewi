from myimports import *

def Connect():
	#db connection
	db = mysql.connector.connect(
		host = "<your host>",
		user = "<your user>",
		passwd = "<your pwd>",
		db = "<your db>"
	)

	cur = db.cursor()

	cur.execute("<select query>")

	myresult = cur.fetchall()

	df = DataFrame(myresult)
	df_len = len(df.index)
	if df_len == 0:
		print("No Requests")
		sys.exit(1)

	df.columns = cur.column_names

	return df

def Update(id_req,country):
	#db connection
	db = mysql.connector.connect(
		host = "<your host>",
		user = "<your user>",
		passwd = "<your pwd>",
		db = "<your db>"
	)

	cur = db.cursor()

	sql = "<update query>"
	cur.execute(sql)
	#print(cur.rowcount, "record(s) affected")
	db.commit()

def Insert(id_req,rev_count,country):
	#db connection
	db = mysql.connector.connect(
		host = "<your host>",
		user = "<your user>",
		passwd = "<your pwd>",
		db = "<your db>"
	)

	cur = db.cursor()

	stat_insert = "<insert query>"
	cur.execute(stat_insert)
	db.commit()

def Update_main(id_req):
	#db connection
	db = mysql.connector.connect(
		host = "<your host>",
		user = "<your user>",
		passwd = "<your pwd>",
		db = "<your db>"
	)

	cur = db.cursor()

	sql_ex = "<update query>"
	cur.execute(sql_ex)
	print(cur.rowcount, "record(s) affected")
	db.commit()
