import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        creds = Credentials.from_service_account_file(
            "Day39and40_FlightCheck/creds.json", scopes=scopes
        )
        client = gspread.authorize(creds)
        sheet_id = "1e6plRXxr5XqPTV4BJpKA2Bvgii1E6w7rPUsir4yGjZo"

        self.sheet = client.open_by_key(sheet_id)

    def get_data(self):
        return pd.DataFrame(self.sheet.sheet1.get_all_records())

    def update_data(self, df: pd.DataFrame):
        self.sheet.sheet1.update([df.columns.values.tolist()] + df.values.tolist())
