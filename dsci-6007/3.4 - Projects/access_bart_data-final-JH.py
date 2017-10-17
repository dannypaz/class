#! usr/bin/env python
#http://www.blog.pythonlibrary.org/2010/11/20/python-parsing-xml-with-lxml/
__author__='Jonathan Hilgart'
import requests
from lxml import etree
from StringIO import StringIO
import pandas as pd
import datetime
import pytz
import time

SF_time = pytz.timezone('US/Pacific')
current_sf_time = datetime.datetime.now(SF_time)
raw_time_sf = time.strftime('{}'.format(current_sf_time)).split(' ')
print('{}'.format(raw_time_sf[1],),'SF time')

#print('{}:{}{}'.format(hour,tens,minutes))

## Access the bart api
bart_key = 'QUZL-PQ66-9XYT-DWE9'
payload = {'cmd': 'etd', 'orig': '16th','dir':'n','key':bart_key}


#http://api.bart.gov/api/etd.aspx?cmd=etd&orig=12th&key=MW9S-E7SL-26DU-VV8V
r = requests.get('http://api.bart.gov/api/etd.aspx',\
params=payload)
print(r.status_code)
content = r.content
print(type(content)),'content'
print(type(r),'type')

print(r.encoding,'encoding')
bart_df_list = []

tree = etree.parse(StringIO(content))
context = etree.iterparse(StringIO(content))
for action, elem in context:
    if not elem.text:
        text = "None"
    else:
        text = elem.text
    if elem.tag =='name':
        origin_station=elem.tag
    elif elem.tag =='destination':
        destination_station=elem.tag
    print elem.tag + " => " + text
## NAME is the orig station, where the car is now, destination is where
#the train is heading


##stations
# 12th	12th St. Oakland City Center
# 16th	16th St. Mission (SF)
# 19th	19th St. Oakland
# 24th	24th St. Mission (SF)
# ashb	Ashby (Berkeley)
# balb	Balboa Park (SF)
# bayf	Bay Fair (San Leandro)
# cast	Castro Valley
# civc	Civic Center (SF)
# cols	Coliseum
# colm	Colma
# conc	Concord
# daly	Daly City
# dbrk	Downtown Berkeley
# dubl	Dublin/Pleasanton
# deln	El Cerrito del Norte
# plza	El Cerrito Plaza
# embr	Embarcadero (SF)
# frmt	Fremont
# ftvl	Fruitvale (Oakland)
# glen	Glen Park (SF)
# hayw	Hayward
# lafy	Lafayette
# lake	Lake Merritt (Oakland)
# mcar	MacArthur (Oakland)
# mlbr	Millbrae
# mont	Montgomery St. (SF)
# nbrk	North Berkeley
# ncon	North Concord/Martinez
# oakl	Oakland Int'l Airport
# orin	Orinda
# pitt	Pittsburg/Bay Point
# phil	Pleasant Hill
# powl	Powell St. (SF)
# rich	Richmond
# rock	Rockridge (Oakland)
# sbrn	San Bruno
# sfia	San Francisco Int'l Airport
# sanl	San Leandro
# shay	South Hayward
# ssan	South San Francisco
# ucty	Union City
# warm	Warm Springs/South Fremont
# wcrk	Walnut Creek
# wdub	West Dublin
# woak	West Oakland
