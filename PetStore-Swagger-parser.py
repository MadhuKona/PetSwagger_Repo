#!/usr/local/bin/python3

# script to automatically fetch swagger jon and extract API endpoints

# import required python modules here
import json
import requests

# swagger URL
swagger_url = "https://petstore.swagger.io/v2/swagger.json"

# fetch swagger json
response = requests.get(swagger_url)

if 200 <= response.status_code <= 299:
    # extract API end points from swagger json
    swagger_json = json.loads(response.text)
    paths = swagger_json['paths']
    print("Swagger API endpoints:")
    for endpoint in paths:
        print("  ", endpoint)
else:
    print("ERRO: Failed to fetch json from swagger URL %s, erro code: %d" % (swagger_url, response.status_code))
