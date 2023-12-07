class BusStop:
    def __init__(self, id: int, name: str, latitude:float, longitude: float, ):
        self._id = id
        self._name = name
        self._latitude = latitude
        self._longitude = longitude

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        self._name = new_name

    def get_location(self) -> tuple[float, float]:
        return self._latitude, self._longitude

    def set_location(self, latitude, longitude) -> None:
        self._latitude = latitude
        self._longitude = longitude
