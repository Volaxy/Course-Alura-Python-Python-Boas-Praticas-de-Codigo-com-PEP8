from queue import Queue
from constraints import NORMAL_CODE


class NormalQueue(Queue):
    def generate_current_password(self) -> None:
        self.current_password = f"{NORMAL_CODE}{self.code}"

    def call_client(self, cashier: int) -> str:
        current_client = self.queue.pop(0)
        self.customers_served.append(current_client)

        return f"Current Client: {current_client}, go to the cashier: {cashier}"
