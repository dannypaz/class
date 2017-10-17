#! usr/bin/end python
__author__='Jonathan Hilgart'
import requests
import yaml
import os
import json
credentials = yaml.load(open(os.path.expanduser('~/data_engineering_final_credentials.yml')))
# SF city id 5391997
weather_key = credentials['open_weather'].get('key')
# units:imperial returns temp in fahrenheit
payload_routes = {'command': 'routelist', 'a:':'sf-muni'}
payload_predictions = {'command':'predictions', 'a':'sf-muni', 'stopId':'15584'} ## predictions for a given stop
payload_route_config ={'command':'routeConfig', 'a':'sf-muni', 'r':'E'} # r is route tag
#http://api.bart.gov/api/etd.aspx?cmd=etd&orig=12th&key=MW9S-E7SL-26DU-VV8V
#http://webservices.nextbus.com/service/publicXMLFeed?command=commandNam
#e&a=<agency tag>&

r = requests.get('http://webservices.nextbus.com/service/publicXMLFeed?',\
params=payload_predictions)
print(r.content)
content = json.loads(r.content)

print(content,'all content')



# <route tag="E" title="E-Embarcadero"/>
# <route tag="F" title="F-Market & Wharves"/>
# <route tag="J" title="J-Church"/>
# <route tag="KT" title="KT-Ingleside/Third Street"/>
# <route tag="L" title="L-Taraval"/>
# <route tag="M" title="M-Ocean View"/>
# <route tag="N" title="N-Judah"/>
# <route tag="NX" title="NX-Express"/>
# <route tag="1" title="1-California"/>
# <route tag="1AX" title="1AX-California A Express"/>
# <route tag="1BX" title="1BX-California B Express"/>
# <route tag="2" title="2-Clement"/>
# <route tag="3" title="3-Jackson"/>
# <route tag="5" title="5-Fulton"/>
# <route tag="5R" title="5R-Fulton Rapid"/>
# <route tag="6" title="6-Haight-Parnassus"/>
# <route tag="7" title="7-Haight-Noriega"/>
# <route tag="7R" title="7R-Haight-Noriega Rapid"/>
# <route tag="7X" title="7X-Noriega Express"/>
# <route tag="8" title="8-Bayshore"/>
# <route tag="8AX" title="8AX-Bayshore A Express"/>
# <route tag="8BX" title="8BX-Bayshore B Express"/>
# <route tag="9" title="9-San Bruno"/>
# <route tag="9R" title="9R-San Bruno Rapid"/>
# <route tag="10" title="10-Townsend"/>
# <route tag="12" title="12-Folsom-Pacific"/>
# <route tag="14" title="14-Mission"/>
# <route tag="14R" title="14R-Mission Rapid"/>
# <route tag="14X" title="14X-Mission Express"/>
# <route tag="18" title="18-46th Avenue"/>
# <route tag="19" title="19-Polk"/>
# <route tag="21" title="21-Hayes"/>
# <route tag="22" title="22-Fillmore"/>
# <route tag="23" title="23-Monterey"/>
# <route tag="24" title="24-Divisadero"/>
# <route tag="25" title="25-Treasure Island"/>
# <route tag="27" title="27-Bryant"/>
# <route tag="28" title="28-19th Avenue"/>
# <route tag="28R" title="28R-19th Avenue Rapid"/>
# <route tag="29" title="29-Sunset"/>
# <route tag="30" title="30-Stockton"/>
# <route tag="30X" title="30X-Marina Express"/>
# <route tag="31" title="31-Balboa"/>
# <route tag="31AX" title="31AX-Balboa A Express"/>
# <route tag="31BX" title="31BX-Balboa B Express"/>
# <route tag="33" title="33-Ashbury-18th St"/>
# <route tag="35" title="35-Eureka"/>
# <route tag="36" title="36-Teresita"/>
# <route tag="37" title="37-Corbett"/>
# <route tag="38" title="38-Geary"/>
# <route tag="38R" title="38R-Geary Rapid"/>
# <route tag="38AX" title="38AX-Geary A Express"/>
# <route tag="38BX" title="38BX-Geary B Express"/>
# <route tag="39" title="39-Coit"/>
# <route tag="41" title="41-Union"/>
# <route tag="43" title="43-Masonic"/>
# <route tag="44" title="44-O'Shaughnessy"/>
# <route tag="45" title="45-Union-Stockton"/>
# <route tag="47" title="47-Van Ness"/>
# <route tag="48" title="48-Quintara-24th Street"/>
# <route tag="49" title="49-Van Ness-Mission"/>
# <route tag="52" title="52-Excelsior"/>
# <route tag="54" title="54-Felton"/>
# <route tag="55" title="55-16th Street"/>
# <route tag="56" title="56-Rutland"/>
# <route tag="57" title="57-Parkmerced"/>
# <route tag="66" title="66-Quintara"/>
# <route tag="67" title="67-Bernal Heights"/>
# <route tag="76X" title="76X-Marin Headlands Express"/>
# <route tag="81X" title="81X-Caltrain Express"/>
# <route tag="82X" title="82X-Levi Plaza Express"/>
# <route tag="83X" title="83X-Mid-Market Express"/>
# <route tag="88" title="88-Bart Shuttle"/>
# <route tag="90" title="90-San Bruno Owl"/>
# <route tag="91" title="91-Owl"/>
# <route tag="K_OWL" title="K-Owl"/>
# <route tag="L_OWL" title="L-Owl"/>
# <route tag="M_OWL" title="M-Owl"/>
# <route tag="N_OWL" title="N-Owl"/>
# <route tag="T_OWL" title="T-Owl"/>
# <route tag="59" title="Powell/Mason Cable Car"/>
# <route tag="60" title="Powell/Hyde Cable Car"/>
# <route tag="61" title="California Cable Car"/>
# </body>
