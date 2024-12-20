import requests
from config import FLIGHT_API_KEY, FLIGHT_API_SECRET


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_url = "https://test.api.amadeus.com/v2"
        self.token = self.get_token()["access_token"]

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

    def get_city_code(self, cityname: str):
        url = self.api_url + "/reference-data/locations/cities"
        header = {"authorization": f"Bearer {self.token}"}
        parameters = {"keyword": cityname, "max": 1}
        response = requests.get(url=url, headers=header, params=parameters)
        data = response.json()
        return data["data"][0]["iataCode"]

    def get_flights(self, dest: str, start_day: str, return_day: str):
        url = self.api_url + "/shopping/flight-offers"
        header = {"authorization": f"Bearer {self.token}"}
        parameters = {
            "originLocationCode": "VIE",
            "destinationLocationCode": dest,
            "departureDate": start_day,
            "returnDate": return_day,
            "adults": 1,
        }
        response = requests.get(url=url, params=parameters, headers=header)
        return response.json()
