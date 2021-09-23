import http.client
import json
import sys
import urllib.parse


def filted_message():
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

    json_str = json.dumps(target_json, indent=4)
    print(json_str)

    message = target_json['message']
    subtitle = target_json['subtitle']
    return message, subtitle


