import requests
import logging
import json
import csv
from lxml import html


def get_headers():
    cookies = []
    session = requests.Session()

    cookie = session.get("https://www.zillow.com/").cookies.get_dict()

    for key in cookie:
        cookies.append(key + "=" + cookie[key])

    headers = {
        'authority': 'www.zillow.com',
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'cookie': "; ".join(cookies),
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://www.zillow.com/agent-finder/real-estate-agent-reviews/?name=Gregg%20Van%20Orden',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    return headers


def post_headers():
    cookies = []
    session = requests.Session()

    cookie = session.get("https://www.zillow.com/").cookies.get_dict()

    for key in cookie:
        cookies.append(key + "=" + cookie[key])

    headers = {
        'authority': 'www.zillow.com',
        'method': 'POST',
        'path': '/graphql/',
        'content-type': 'text/plain',
        'connection': 'keep-alive',
        'cookie': "; ".join(cookies),
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US',
        'cache-control': 'no-cache',
        'content-length': '20000',
        'referer': 'https://www.zillow.com/homedetails/',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    return headers


def payload(zpid, property_type):
    if property_type == 'rent':
        payload = {
            "clientVersion": "home-details/5.45.3.14.master.4008e7b",
            "operationName": "ForRentDoubleScrollFullRenderQuery",
            "queryId": "b9c181517907bf9cad3bc97db77a2e18",
            "variables": {"zpid": zpid, "contactFormRenderParameter": {"zpid": zpid, "platform": "desktop", "isDoubleScroll": True}}
        }

    if property_type == 'sale':
        payload = {
            "operationName": "ForSaleDoubleScrollFullRenderQuery",
            "variables": {"zpid": int(zpid)},
            "queryId": "f59fb6f9ceace205052147034dd63615"
        }

    if property_type == 'offmarket':
        payload = {
            "operationName": "OffMarketFullRenderQuery",
            "variables": {"zpid": zpid},
            "queryId": "ace848b8c9e7169862ad693de7a14cb6"
        }

    return payload


def get_property(zpid):
    results = {}
    property_types = ['rent', 'sale', 'offmarket']

    for property_type in property_types:
        try:
            request = requests.post("https://www.zillow.com/graphql/",
                                    data=json.dumps(payload(zpid, property_type)), headers=post_headers())

            response = json.loads(request.text)
            prop = response['data']['property']
        except:
            continue

        for key in prop:
            if isinstance(prop[key], (type({}))):
                if key == "address":
                    for add in prop[key]:
                        results[add] = prop[key][add]
                elif key == "homeFacts":
                    i = 0
                    facts = prop[key]['atAGlanceFacts']
                    while i < len(facts):
                        results[facts[i]['factLabel']] = facts[i]['factValue']
                        i += 1

            elif isinstance(prop[key], (type([]))):
                if key == 'responsivePhotos':
                    photos = prop[key][0]['mixedSources']['jpeg']
                    results['photos'] = photos
            else:
                results[key] = prop[key]

    with open(zpid + '.csv', 'w', newline='') as prop_file:
        prop_writer = csv.writer(
            prop_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for key in results:
            print(key, results[key])
            prop_writer.writerow([key, results[key]])
