from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey


def connect(user, password, db, host='127.0.0.1', port=5432):
	"""Return a connection and a metadata object"""
	# postgresql://user1:user1@127.0.0.1:5432/tennis
	url = 'postgresql://{0}:{1}@{2}:{3}/{4}'
	url = url.format(user, password, host, port, db)

	# The return value of create_engine() is our connection object
	con = create_engine(url, client_encoding='utf8')

	# We then bind the connection to Metadata()
	meta = MetaData(bind = con, reflect = True)

	return con, meta

def add_tables(con, meta):
	slams = Table('slams', meta,
		Column('name', String, primary_key = True),
		Column('country', String)
	)

	results = Table('results', meta,
		Column('slam', String, ForeignKey('slams.name')),
		Column('year', Integer),
		Column('result', String)
	)
	meta.create_all(con)

def add_records(con, meta):
	candidates = [
		{'name': 'Wimbledon', 'country': 'United Kingdom'},
		{'name': 'Roland Garros', 'country': 'France'}
	]
	victories = [
		{'slam': 'Wimbledon', 'year': 2003, 'result': 'W'},
		{'slam': 'Wimbledon', 'year': 2004, 'result': 'W'},
		{'slam': 'Wimbledon', 'year': 2005, 'result': 'W'}
	]
	con.execute(meta.tables['slams'].insert(), candidates)
	con.execute(meta.tables['results'].insert(), victories)

def check_db(meta):
	results = meta.tables['results']
	for col in results.c:
		print(col)

def select_records(con, meta):
	results = meta.tables['results']
	for row in con.execute(results.select()):
		print(row)
	clause = results.select().where(results.c.year == 2005)
	for row in con.execute(clause):
		print('***', row, '***')
