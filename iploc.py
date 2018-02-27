## iploc.py - IPGeolocation
# -*- coding: utf-8 -*-
## Author: DedSecTL/DTL
## Date: 24-01-2018 (08:00)
## Github: https://github.com/Gameye98
## Team: BlackHole Security
import os
import json
import urllib

__banner__ = """
 .iVVVVVVi
 |       |  .___ __________ .____                     
 |       |  |   |\______   \|    |      ____    ____  
 |  (O) (O) |   | |     ___/|    |     /  _ \ _/ ___\ 
C       _)  |   | |    |    |    |___ (  <_> )\  \___ 
 |    ,_|   |___| |____|    |_______ \ \____/  \___  >
 |      /                           \/             \/ 
 |     /
"""

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

print __banner__
iphost = raw_input("IP or Hostname: ")
url = "https://tools.keycdn.com/geo.json?host=%s" %iphost
geoip = urllib.urlopen(url).read()
geoipdata = geoip.replace('{"status":"success","description":"Data successfully received.","data":{"geo":', '')
geodata = geoipdata.replace('}}', '')

try:
	file = open("status.json", 'w')
	file.write(geoip)
	file.close()
	file = open("data.json", 'w')
	file.write(geodata)
	file.close()
	file = open("status.json")
	status = json.load(file)
	file = open("data.json")
	data = json.load(file)
	print('\nHost: ' + data["host"])
	print('IP: ' + data["ip"])
	print('RDNS: ' + data["rdns"])
	print('ASN: ' + data["asn"])
	print('ISP: ' + data["isp"])
	print('Country: ' + data["country_name"])
	print('Country Code: ' + data["country_code"])
	print('Region: ' + data["region"])
	print('City: ' + data["city"])
	print('Postal Code: ' + data["postal_code"])
	print('Continent Code: ' + data["continent_code"])
	print('Latitude: ' + data["latitude"])
	print('Longitude: ' + data["longitude"])
	print('DMA Code: ' + data["dma_code"])
	print('Area Code: ' + data["area_code"])
	print('Timezone: ' + data["timezone"])
	print('Datetime: ' + data["datetime"])
	print('Status: ' + status["status"])
	os.remove("status.json")
	os.remove("data.json")
except IOError, e:
	print "[!] ERROR:",e
	sys.exit()