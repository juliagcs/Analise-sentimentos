import requests
import os
import csv
import json
from datetime import date

dia = date.today()

filename = open("fundosListados.csv", "r")

arquivo = csv.DictReader(filename)

nomes = []
files = []

for coluna in arquivo:
    cod = coluna["codigo"]
    nomes.append(cod)
    files.append(open(f"{dia}-{cod}.json", "x"))

bearer_token = "AAAAAAAAAAAAAAAAAAAAACahdQEAAAAArDJtUMLTAQ94qBb7Oocib%2FBOIX8%3DInNK6YOs5ya025nmNGWZNSsD6DdCPaOOivHh5Jnsva3NdiYG9a"

search_url = "https://api.twitter.com/2/tweets/search/recent"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main(name, i):
    query_params = {"query":name,"max_results":100, "place.fields": { "country_code": "BR" }}
    json_response = connect_to_endpoint(search_url, query_params)
    files[i].write(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    i=0;
    for n in nomes:
        main(n, i)
        i = i+1

    for f in files:
        f.close()
