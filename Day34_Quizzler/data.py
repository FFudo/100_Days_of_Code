import requests


def get_data():
    parameters = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]


question_data = get_data()
