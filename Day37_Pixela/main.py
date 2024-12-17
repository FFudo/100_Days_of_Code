import requests
from config import TOKEN, USERNAME
import datetime as dt


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

# response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(response.text)

def post_pixel(n):
    pixel_endpoint = f"{graph_endpoint}/{graph_params["id"]}"

    today = str(dt.datetime.now().date())
    today = today.replace("-", "")

    pixel_params = {
        "date": today,
        "quantity": str(n),
    }
    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
    print(response.text)

def update_pixel(n, day: str):
    pixel_endpoint = f"{graph_endpoint}/{graph_params["id"]}/{day}"

    pixel_params = {
        "quantity": str(n),
    }
    response = requests.put(url=pixel_endpoint, json=pixel_params, headers=header)
    print(response.text)

def delete_pixel(day: str):
    pixel_endpoint = f"{graph_endpoint}/{graph_params["id"]}/{day}"
    
    response = requests.delete(url=pixel_endpoint, headers=header)
    print(response.text)

delete_pixel("20241217")