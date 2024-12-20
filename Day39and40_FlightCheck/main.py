from flight_data import FlightDataManager


def run_app():
    flight_data = FlightDataManager()
    flight_data.update_city_code()
    flight_data.update_flight_price()


if __name__ == "__main__":
    run_app()
