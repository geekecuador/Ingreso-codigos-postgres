import psycopg2
import sys

def main():
	conn_string = "host='demo' dbname='demo' user='demo' password='demo'"
 	
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
	conn.autocommit = True
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n"
	lines = [line.rstrip('\n') for line in open('codigos20.txt')]
	for codigo in lines:
		sql  = "INSERT INTO public.mashca_codigo(activo, id, codigo, valor, proyecto_id) VALUES (true,DEFAULT,'"+codigo+"', 20, 2);"
		print sql
		cursor.execute(sql)

if __name__ == '__main__':
	main()
