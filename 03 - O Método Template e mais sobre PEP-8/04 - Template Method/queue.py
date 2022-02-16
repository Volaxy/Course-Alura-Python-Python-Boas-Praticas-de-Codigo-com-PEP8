import abc


class Queue(metaclass=abc.ABCMeta):
    code: int = 0
    queue = []
    customers_served = []
    current_password: str = ""

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()

    def insert_client(self):
        self.queue.append(self.current_password)

    # This method forces the child classes to implement it
    @abc.abstractmethod
    def generate_current_password(self):
        ...

    @abc.abstractmethod
    def call_client(self, cashier: int):
        ...
