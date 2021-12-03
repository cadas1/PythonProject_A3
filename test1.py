import json

import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

parameters= {
    "lat": 16.92,
    "lon": 145.77
}

response2= requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
jprint(response2.json())
