import abc
from typing import List

from constraints import MINIMUM_STANDARD_SIZE, SIZE_STANDARD_MAXIMUM


class Queue(metaclass=abc.ABCMeta):
    code: int = 0
    queue: List[str] = []
    customers_served: List[str] = []
    current_password: str = ""

    def reset_queue(self) -> None:
        if self.code >= SIZE_STANDARD_MAXIMUM:
            self.code = MINIMUM_STANDARD_SIZE
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()

    def insert_client(self):
        self.queue.append(self.current_password)

    @abc.abstractmethod
    def generate_current_password(self):
        ...

    @abc.abstractmethod
    def call_client(self, cashier: int):
        ...
