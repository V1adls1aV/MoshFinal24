from .api import Api
from datetime import datetime
from ..models import InfoByDate


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
        data = InfoByDate.parse_obj(body)

        return data
