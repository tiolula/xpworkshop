import requests

url = "https://openexchangerates.org/api/latest.json?app_id=<pegue no https://openexchangerates.org/account/app-ids>&symbols=<moeda esperada>"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)