import requests
from config import TOKEN, USERNAME

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "push up graph",
    "unit": "times",
    "type": "int",
    "color": "momiji",
}

header = {"X-USER-TOKEN": TOKEN}

response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
print(response.text)