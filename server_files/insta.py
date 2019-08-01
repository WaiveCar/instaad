import requests, sys, pymysql

def instag (access):
    url = "https://api.instagram.com/v1/users/self/"
    r_info = requests.get(url, {'access_token' : access})
    r_media = requests.get(url+"media/recent/", {'access_token' : access})
    print(r_info.url)
    print(r_media.url)

instag(sys.argv[1:2])
