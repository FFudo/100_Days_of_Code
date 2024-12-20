from datetime import datetime, timedelta

import pandas as pd
from data_manager import DataManager
from flight_search import FlightSearch


class FlightDataManager:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.data_manager = DataManager()
        self.df = self.data_manager.get_data()
        self.flight_search = FlightSearch()

    def update_city_code(self):
        update = False
        for index, row in self.df.iterrows():
            if row["IATA Code"] == "":
                self.df.loc[index, "IATA Code"] = self.flight_search.get_city_code(
                    row["City"]
                )
                update = True

        if update:
            self.data_manager.update_data(self.df)

    def update_flight_price(self):
        tommorow = datetime.now() + timedelta(days=1)
        tommorow = tommorow.strftime("%Y-%m-%d")
        in_six_month = datetime.now() + timedelta(days=(6 * 30))
        in_six_month = in_six_month.strftime("%Y-%m-%d")

        update = False
        for index, row in self.df.iterrows():
            if row["Lowest Price"] == "":
                self.df.loc[index, "Lowest Price"] = 50000.00

            flights = self.flight_search.get_flights(
                dest=row["IATA Code"], start_day=tommorow, return_day=in_six_month
            )
            cheapest_flight = get_cheapest_flight(flights)

            if cheapest_flight and cheapest_flight.price < float(row["Lowest Price"]):
                self.df.loc[index, "Lowest Price"] = cheapest_flight.price
                self.df.loc[index, "Departure"] = cheapest_flight.departure_date
                self.df.loc[index, "Return"] = cheapest_flight.return_date
                self.df.loc[index, "Flight Number"] = cheapest_flight.number
                update = True

        if update:
            self.data_manager.update_data(self.df)


class FlightData:
    def __init__(self, origin, price, destination, departure, back, flightnumber):
        self.origin = origin
        self.destination = destination
        self.price = price
        self.departure_date = departure
        self.return_date = back
        self.number = flightnumber


def get_cheapest_flight(flights) -> FlightData:
    try:
        flights["data"][0]
    except IndexError:
        return None

    first_flight = flights["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split(
        "T"
    )[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"][
        "at"
    ].split("T")[0]
    flightnumber = (
        first_flight["itineraries"][0]["segments"][0]["carrierCode"]
        + first_flight["itineraries"][0]["segments"][0]["number"]
    )

    cheapest_flight = FlightData(
        origin, lowest_price, destination, out_date, return_date, flightnumber
    )

    for flight in flights["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split(
                "T"
            )[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"][
                "at"
            ].split("T")[0]
            flightnumber = (
                flight["itineraries"][0]["segments"][0]["carrierCode"]
                + flight["itineraries"][0]["segments"][0]["number"]
            )
            cheapest_flight = FlightData(
                lowest_price, origin, destination, out_date, return_date, flightnumber
            )

    return cheapest_flight
