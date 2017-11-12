import json
from urllib.request import urlopen


def get_country(ip_address):
    response = urlopen("http://freegeoip.net/json/" + ip_address).read().decode('utf-8')

    response_json = json.loads(response)
    return response_json.get("country_code")


print(get_country("50.78.253.58"))