import sys
import requests
from jinja2 import Template

campaign_id = sys.argv[1]
campaign_post = requests.get("http://www.waivescreen.com/api/campaign",params={'id':campaign_id})
text = campaign_post.json();
lat = text[0]["lat"]
lng = text[0]["lng"]
print(type(text))
print(type(text[0]))
print(type(text[0]['lat']))
print(lat)
print(lng)

rendered = Template(open('heatmap.html').read()).render(lat=lat,lng=lng);

text_file = open("email/first_day/"+campaign_id+".html", "w")
text_file.write(rendered)
text_file.close()

iframe = "<iframe src ='email/first_day/'"+campaign_id+"'.html' width ='100%'> </iframe>"
print(iframe)
