import requests
import json

url = "https://rapidapi.com/apidojo/api/realtor/"

#making a GET request to the app
response = requests.get(url)

print(response.text)
#json_content = json.loads(response.text)