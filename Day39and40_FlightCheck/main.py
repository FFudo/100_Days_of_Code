from data_manager import DataManager
from flight_search import FlightSearch


def run_app():
    data_manager = DataManager()
    data = data_manager.get_data()
    flight_search = FlightSearch()


if __name__ == "__main__":
    run_app()
