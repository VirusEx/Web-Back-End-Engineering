import http.client
import json
import sys
import urllib.parse


def redacted_message():
    foaas = http.client.HTTPSConnection("foaas.com")
    Purgo = http.client.HTTPSConnection("www.purgomalum.com")

    foaas_headers = {'Accept' : 'application/json'}
    foaas.request("GET", sys.argv[1], headers=foaas_headers)
    foaas_response = foaas.getresponse()
    target_json = json.loads(foaas_response.read())
    query = urllib.parse.quote(target_json['message'])

    Purgo.request("GET", "/service/json?text=" + query)
    Purgo_response = Purgo.getresponse()
    flitered_message = json.loads(Purgo_response.read())
    target_json['message'] = flitered_message['result']

    return target_json


if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   json_str = json.dumps(redacted_message(), indent=4)
   print(json_str)

