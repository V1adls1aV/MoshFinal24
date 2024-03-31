from .api import Api
from datetime import datetime
from ..models import *


class MietApi:
    def __init__(self) -> None:
        self.api = Api()

    def get_dates(self) -> list[datetime]:
        response = self.api.get("/date").json()

        dates = []
        for date_str in response["message"]:
            dates.append(datetime.strptime(date_str, "%d-%m-%y").date())

        return dates

    def get_info_by_date(self, date: datetime):
        params = {"day": date.day, "month": date.month, "year": str(date.year)[-2:]}
        response = self.api.get("", params=params)

        body = response.json()["message"]
        info_date = Date.parse_obj(body["date"])
        flats_count = FlatsCount.parse_obj(body["flats_count"])

        window_floors = []
        for i in range(flats_count.data):
            window_floors.append(body["windows"]["data"][f"floor_{i+1}"])

        print(window_floors)

        window = Windows(data=window_floors, description=body["windows"]["description"])
        windows_for_flat = WindowsForFlat.parse_obj(body["windows_for_flat"])

        return InfoByDate(
            date=info_date,
            flats_count=flats_count,
            windows=window,
            windows_for_flat=windows_for_flat
        )
