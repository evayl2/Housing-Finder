import json
import requests

form_data = {
        "username": "some username",
        "password": "some password",
        "major": "some major",
        "groupNum": "some groupNum",
        "description": "some description"
        }

url = 'https://yw882wh1rc.execute-api.us-east-1.amazonaws.com/dev/users'

response = requests.post(url, data=json.dumps(form_data))
print(response)
