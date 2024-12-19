from data_manager import DataManager


def run_app():
    data_manager = DataManager()
    data = data_manager.get_data()
    print(data)


if __name__ == "__main__":
    run_app()
