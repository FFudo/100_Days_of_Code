from data_manager import DataManager
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.data_manager = DataManager()
        self.df = self.data_manager.get_data()

        self.flight_search = FlightSearch()