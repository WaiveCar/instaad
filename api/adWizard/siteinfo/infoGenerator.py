import json
import requests as req
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as soup
import pprint
import re
import pdb


yelp = "https://api.yelp.com/v3/businesses/"
api_key = "KhDk516rsRCrgrlwl16HC4kPOTNzZxVlrHmXk-LA1fQ7WfSPiu7B_E3qQ8usA7f7mbqmaYfZkmSx7cphaVE15cjIu-pU_5P92W6t5msCX66Ta9Svidk5SUAM8YXjXHYx"
def generate(site):
    if site[0:4] != "http":
        site = "http://" + site

    try:
        response = req.get(site)
    except HTTPError:
        print('HTTP error occured: ',HTTPError)
        quit()
    except Exception:
        print('Error occured: ',Exception)
        quit()
    print(site)
    #I don't know if this is necessary
    ###############
    if(response.status_code != 200):
        print("Reached ",response.status_code," error. Program will now exit")
        quit()
    ################
    bs = soup(response.content, "html.parser")
    dict = {}
    ################################################
    ### Start of search for different info
    information = {
    'facebook','instagram','twitter','email','logo','phone','address', 'hours'
    }
    unobtainedinfo = []
    social_media = ('facebook','instagram','twitter')
    for info in information:
        ###Social Media
        element = None
        for sm in social_media:
            if (info == sm):
                element = bs.find(
                    href = {re.compile(sm)}
                    )
                if(element == None):
                    print(sm, "account is not found")
                    unobtainedinfo.append(sm)
                    continue
                href = element['href']
                print(sm, href)
                dict[sm] = href
                continue
        ###Email
        if (info == 'email'):
            for bsele in bs.find_all(class_ = {re.compile("(e(-)*mail)")}):
                if (bsele['href'] != None):
                    element = bsele
                    break
            if (element == None):
                print("E-Mail is not found")
                unobtainedinfo.append(info)
                continue
            if(element['href'][0:6] == "mailto"):
                element['href'] = element['href'][7:len(element['href'])]
                print(info, element['href'])
            dict[info] = element['href']
            continue
        ###Logo
        ### Just curl the website and grep looking for jpeg or png and then
        ### look through the pic with the highest memory
        if (info == 'logo'):
            '''
            element = bs.find(
                href = {re.compile(sm)}
                )
            '''
            foundEle = False
            #
            for bsele in bs.find_all(src = {re.compile("((L|l)ogo)")}):
                print(bsele)
                src = bsele['src']
                foundEle = True
                print(info, src)
                element = bsele
                dict[info] = src
                foundEle = True
            if (foundEle == False):
                for bsele in bs.find_all(class_ = {re.compile("((L|l)ogo)")}):
                    '''
                    try:
                        src = bsele['src']
                        foundEle = True
                    except Exception:
                        print("No src")
                        continue
                    '''
                    print(bsele)
                    src = bsele['src']
                    print(info, src)
                    print(bsele['src'])
                    element = bsele
                    dict[info] = src
            if (element == None):
                print('Logo not found')
                unobtainedinfo.append(info)
            continue

        ###Phone number
        if (info == 'phone'):
            continue
        ###Address
        if (info == 'address'):
            continue
        ###Business hours
        if (info == 'hours'):
            for bsele in bs.find_all(text = {re.compile("(1|2|3|4|5|6|7|8|9|10|11|12)(pm|PM)")}):
                bsele.parent
            continue

    #print(element['href'])
    print("Dictionary")
    print(dict)
    print("UnobtainedInfo")
    print(unobtainedinfo)

    ###yelp side of town
    '''
    key = {"Authorization" : "Bearer %s" % api_key}
    params = {
    "location" : "LA",
    "term" : "Washingspot"
    }
    search = req.get(url = yelp + "search",headers = key, params = params)
    print(search.json())
    '''
    ###storing the data in a json file
    file = open("test/info.json", "w")
    #file.append()

generate("www.washingspotla.com")
generate("http://five0fourhollywood.com")
