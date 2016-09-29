from database_access import *

if __name__ == '__main__':
	username = input('Enter databse user name: ')
	password = input('Enter database password: ')
	db = input('Enter database name: ')
	host = input('Enter databse host [default localhost]: ') or '127.0.0.1'
	port = input('Enter port number [default 5432]: ') or 5432
	con, meta = connect(username, password, db, host='127.0.0.1', port=5432)
	add_tables(con, meta)
	add_records(con, meta)
	check_db(meta)
	select_records(con, meta)