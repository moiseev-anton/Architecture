from decimal import Decimal
from datetime import datetime

class Ticket:
    def __init__(self, price: Decimal, date: datetime, start_zone: int, finish_zone: int,
                 is_luggage: bool, place: int, road_number: int):
        self._price = price
        self._date = date
        self._startZone = start_zone
        self._finishZone = finish_zone
        self._isLuggage = is_luggage
        self._place = place
        self._roadNumber = road_number

    def get_price(self) -> Decimal:
        return self._price

    def set_price(self, new_price: Decimal) -> None:
        self._price = new_price

    def get_date(self) -> datetime:
        return self._date

    def set_date(self, new_date: datetime) -> None:
        self._date = new_date

    def get_start_zone(self) -> int:
        return self._startZone

    def set_start_zone(self, new_start_zone: int) -> None:
        self._startZone = new_start_zone

    def get_finish_zone(self) -> int:
        return self._finishZone

    def set_finish_zone(self, new_finish_zone: int) -> None:
        self._finishZone = new_finish_zone

    def get_place(self) -> int:
        return self._place

    def set_place(self, new_place: int) -> None:
        self._place = new_place

    def get_is_luggage(self) -> bool:
        return self._isLuggage

    def set_is_luggage(self, new_is_luggage: bool) -> None:
        self._isLuggage = new_is_luggage

    def get_road_number(self) -> int:
        return self._roadNumber

    def set_road_number(self, new_road_number: int) -> None:
        self._roadNumber = new_road_number
