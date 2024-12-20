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

        self.update_city_code()

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
        tommorow = tommorow.strftime("%Y-%m-&d")
        in_six_month = datetime.now() + timedelta(days=(6 * 30))
        in_six_month = in_six_month.strftime("%Y-%m-&d")
        for index, row in self.df.iterrows():
            flights = self.flight_search.get_flights(
                dest=row["IATA Code"], start_day=tommorow, return_day=in_six_month
            )
            flight = self.get_cheapest_flight(flights)

    def get_cheapest_flight(self):
        pass
