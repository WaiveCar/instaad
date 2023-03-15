#Change file name to config.py if in local developemt
#delete file if in production

class Config:
	SECRET_KEY=''
	#sqllite is for development purposes
	SQLALCHEMY_DATABASE_URI='mysql:///root:mysqlsucks@localhost/website'
#	SQLALCHEMY_DATABASE_URI='sqlite:///test.db'
