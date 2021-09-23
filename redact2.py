import urllib.request
import http.client
import json
import requests
import pprint

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://www.foaas.com/because/ProfAvery"
headers={'Accept': 'application/json', 'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
data = response.read() # The data u need

response_info = json.loads(data)
print(response_info['message'])

message = response_info['message']

PurgoResponse = requests.get("https://www.purgomalum.com/service/json?text="+message)
print(PurgoResponse.json()['result'])

# PurgoMalum = "www.purgomalum.com"
# PurgoMalumConnection = http.client.HTTPSConnection(PurgoMalum)
# PurgoHeader = {'Content-Type' : 'json'}
# PurgoMalumConnection.request("GET","/",headers= PurgoHeader)
# PurgoResponse = PurgoMalumConnection.getresponse()
# PurgoHeaders = PurgoResponse.getheader('Content-Type')
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint("Headers: {}".format(PurgoHeaders))
# #PurgoMalumConnection.request("POST",'/')

#r = requests.get(url = PurgoMalum, params = message)
#data = r.json()

# newurl= "https://www.purgomalum.com/service/json?text=" + response_info['message']