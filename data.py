import requests

api = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(api, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
