import json

with open('/etc/config.json') as config_file:
	config = json.load(config_file)

class Config:
	SECRET_KEY=config.get('SECRET_KEY')
	#sqllite is for development purposes
	SQLALCHEMY_DATABASE_URI=config.get('SQLALCHEMY_DATABASE_URI')
      #  IG_CLIENT_ID=config.get('IG_CLIENT_ID')
      #  IG_CLIENT_SECRET=config.get('IG_CLIENT_SECRET')
