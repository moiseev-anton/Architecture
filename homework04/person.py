class Person:
    def __init__(self, id: int, fio: str, card_number: int, login: str, hash_pass: int):
        self._id = id
        self._fio = fio
        self._card_number = card_number
        self._login = login
        self._hash_pass = hash_pass

    def get_id(self) -> int:
        return self._id

    def get_fio(self) -> str:
        return self._fio

    def set_fio(self, new_fio: str) -> None:
        self._fio = new_fio

    def get_card_number(self) -> int:
        return self._card_number

    def set_card_number(self, new_card_number: int) -> None:
        self._card_number = new_card_number

    def get_login(self) -> str:
        return self._login

    def set_login(self, new_login: str) -> None:
        self._login = new_login

    def get_hash_pass(self) -> int:
        return self._hash_pass

    def set_hash_pass(self, new_hash_pass: int) -> None:
        self._hash_pass = new_hash_pass
