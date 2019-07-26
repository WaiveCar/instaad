import sys
import datetime
import random
import requests
import string
import json
import _mysql #apt-get install python3-mysqldb

access_token = sys.argv[1]
#query_code = sys.argv[2]

base_url = "https://api.instagram.com/v1/users/self/"
r_info = requests.get(base_url, {'access_token' : access_token})
r_dict = json.loads(r_info.text)
r_dict_data = r_dict["data"]
r_dict_counts = r_dict_data["counts"]

data_field_names = ["id","username","profile_picture","full_name","bio","website","is_business"]
counts_field_names = ["media","follows","followed_by"]

r_media = requests.get(base_url+"media/recent/", {'access_token' : access_token})
timestamp = datetime.datetime.utcnow()
entry_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))

db_conn = _mysql.connect(user="pyuser",passwd="t34igj",db='instaad_db')
db_conn.query("INSERT INTO user_data SET entry_id = '"+str(entry_id)+"';")
db_conn.query("UPDATE user_data SET timestamp = '"+str(timestamp)+"' WHERE entry_id = '"+entry_id+"';")
#db_conn.query("UPDATE user_data SET query_code = '"+str(query_code)+"' WHERE entry_id = '"+entry_id+"';")

for i in data_field_names:
    db_conn.query("UPDATE user_data SET "+i+" = '"+str(r_dict_data[i])+"' WHERE entry_id = '"+entry_id+"';")

for i in counts_field_names:
    db_conn.query("UPDATE user_data SET "+i+" = '"+str(r_dict_counts[i])+"' WHERE entry_id = '"+entry_id+"';")

r_media_dict = json.loads(r_media.text)
r_media_dict_data = r_media_dict["data"]
r_media_dict_images = r_media_dict_data[0]
r_media_dict_images = r_media_dict_images["images"]
r_media_dict_images = r_media_dict_images["standard_resolution"]
r_media_dict_images = r_media_dict_images["url"]
db_conn.query("UPDATE user_data SET most_recent_post = '"+str(r_media_dict_images)+"' WHERE entry_id = '"+entry_id+"';")

r_media_dict = json.loads(r_media.text)
r_media_dict_data = r_media_dict["data"]
r_media_dict_images = r_media_dict_data[1]
r_media_dict_images = r_media_dict_images["images"]
r_media_dict_images = r_media_dict_images["standard_resolution"]
r_media_dict_images = r_media_dict_images["url"]
db_conn.query("UPDATE user_data SET second_post = '"+str(r_media_dict_images)+"' WHERE entry_id = '"+entry_id+"';")

db_conn.close()

print(entry_id)
