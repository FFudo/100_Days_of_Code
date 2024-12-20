import requests
from config import FLIGHT_API_KEY, FLIGHT_API_SECRET


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):

        self.token = self.get_token()

    def get_token(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": FLIGHT_API_KEY,
            "client_secret": FLIGHT_API_SECRET,
        }
        response = requests.post(url=url, headers=header, data=body)
        return response.json()