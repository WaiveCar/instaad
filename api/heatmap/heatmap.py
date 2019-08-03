import sys
import requests
from gmplot import gmplot #pip install gmplot


campaign_id = sys.argv[1]
campaign_post = requests.get("http://www.waivescreen.com/api/campaign",params={'id':campaign_id})
text = campaign_post.json();
if (len(text) == 0):
    print("Campaign does not exist")
    quit()

lat = []
lng = []
for x in text:
    lat.append(x['lat'])
    lng.append(x['lng'])

lat.append(34.0)
lng.append(-118.390432)
lat.append(34.000020)
lng.append(-118.390452)
lat.append(34.000040)
lng.append(-118.390472)


#LA longitude & longitude
gmap = gmplot.GoogleMapPlotter(34.0492, -118.2437, 12)

gmap.heatmap(lat,lng)
# Draw
gmap.draw("my_map.html")
