class TransportZone:
    def __init__(self, id: int, remark: str):
        self._id: int = id
        self._remark: str = remark

    def get_id(self) -> int:
        return self._id

    def get_remark(self) -> str:
        return self._remark

    def set_remark(self, remark: str) -> None:
        self._remark = remark
