import http.client
import json
import sys
import pprint
import urllib
import requests

#print("Argument List:", str(sys.argv))
FOAAS = 'foaas.com'
PurgoMalum = 'www.purgomalum.com'

# print('Test', sys.argv[0])

# {'Content-type': 'application/json'}

# h2.request("GET", "/")
# response = h2.getresponse()
# headers = response.getheaders()
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint("Headers: {}".format(headers))

def _dispatch_request(web):
  
  # conn_path = web + path
  connection = http.client.HTTPSConnection( web)
  headers = {'Accept' : 'application/json'}
  connection.request("GET", "/")
  # response = connection.getresponse()


  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint("Headers: {}".format(headers))
  connection.close()



import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://www.foaas.com/because/ProfAvery"
headers={'Accept': 'application/json', 'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers)
response = urllib.request.urlopen(request)
data = response.read() # The data u need

response_info = json.loads(data)
print(data)



# 'www.foaas.com/because/ProfAvery'


_dispatch_request('www.foaas.com')