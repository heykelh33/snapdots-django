from snapdots.asgi import channel_layer
from channels import  Group
import time
import datetime
import random
import json
import MySQLdb
import sys

DATABASE={'host': 'localhost', 'user': 'root', 'passwd': 'root', 'db': 'sensordb'}


def open_database(host, user, passwd, db):
	conn = MySQLdb.connect(host=host,user=user, passwd=passwd, db=db)    # Open a MySQL database connection
	print("database opened")
	return conn


def save_data_to_database(conn, cursor, type, date_time, data):
	
	cursor.execute("INSERT INTO data (type, date_time, value) values (%s,%s,%s)", (type, date_time, data)) # Execute the SQL command to Insert data to database
	conn.commit()



def push_data_in_channels(data):
	print("Pushing data in channels  " + str(data))
	Group("sensor").send({'text': json.dumps({'text': str(data)})})



if __name__ == '__main__':

	try:
		conn = open_database(DATABASE['host'],DATABASE['user'],DATABASE['passwd'],DATABASE['db'])
		cursor = conn.cursor()      # prepare a cursor object using cursor() method
		
		while True:
			
			datatype=random.choice(['Temperatura','Humedad']) #random choice work with tuple or list
			date_time=datetime.datetime.now()

			if datatype=="Temperatura":
				type=1
				data=float("{0:.2f}".format(random.uniform(20,80)))
			else:
				type=2
				data=random.randint(0,100)

			print type, date_time, data

			save_data_to_database(conn, cursor, type, date_time, data)
			push_data_in_channels(data)

			time.sleep(5)

	except MySQLdb.Error as e:
		print str(e)
		conn.rollback()
		pass			
		
	except KeyboardInterrupt:
		conn.commit()
		sys.exit(1)

	finally:
		if conn:
			cursor.close()
			conn.close()


	


