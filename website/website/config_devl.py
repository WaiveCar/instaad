#Change file name to config.py if in local developemt
#delete file if in production

class Config:
	SECRET_KEY='84e0621dd931baa7e6a014901c6183d5'
	#sqllite is for development purposes
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
