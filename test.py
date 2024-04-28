import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()

url = "http://api.scraperapi.com?"
payload = {'api_key': os.environ['BROWSERLESS_API_KEY'], 'url': 'https://httpbin.org/ip'}
headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
response = requests.get(url, params=payload)

print(response.text)
