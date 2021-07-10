import requests
import random
import json

with open('api.txt') as f:
	tkns = f.readlines()
	tkn = random.choice(tkns).strip()

res1 = requests.get('https://ifconfig.me/ip')
user_ip = res1.text

class IP():
	def __init__(self):
		self.ip = user_ip

	def set_ip(self, i):
		self.ip = i

	def start(self):
		url = f'http://api.ipstack.com/{self.ip}?access_key={tkn}'
		res2 = requests.get(url)
		return json.loads(res2.text)

'''
	GeoIP Location
Your IP : {out["ip"]}
Continent Name : {out["continent_name"]}
Country Name : {out["country_name"]}
Region Name : {out["region_name"]}
City Name : {out["city"]}
Pin Code : {out["zip"]}
Latitude : {out["latitude"]}
Longitude : {out["longitude"]}

	Country Detail
Country Name : {out["country_name"]}
Country Capital : {out["location"]["capital"]}
Country Call Code : {out["location"]["calling_code"]}
'''