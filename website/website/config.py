import os

class Config:
	SECRET_KEY='84e0621dd931baa7e6a014901c6183d5'
	#SECRET_KEY= os.environ.get('SECRET_KEY')
	#sqllite is for development purposes
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	#SECRET_KEY= os.environ.get('SQLALCHEMY_DATABASE_URI')
