from bus_stop import BusStop

class BusRoute:
    def __init__(self, id: int, remark: str, capacity: int, bus_stops: list[BusStop]):
        self._id: int = id
        self._remark: str = remark
        self._capacity: int = capacity
        self._bus_stops: list[BusStop] = bus_stops


    def get_id(self) -> int:
        return self._id

    def get_remark(self) -> str:
        return self.remark

    def set_remark(self, remark: str) -> None:
        self._remark = remark

    def get_capacity(self) -> int:
        return self._capacity

    def set_capacity(self, capacity: int) -> None:
        self._capacity = capacity

    def get_bus_stops(self) -> list[BusStop]:
        return self._bus_stops

    # метод добавляет остановку в начало списка(по умолчанию)
    # или вставляет по указанному индексу
    def insert_bus_stop(self, bus_stop: BusStop, index=0) -> None:
        self._bus_stops.insert(index, bus_stop)

    def remove_bus_stop(self, bus_stop: 'BusStop') -> None:
        if bus_stop in self._bus_stops:
            self._bus_stops.remove(bus_stop)
