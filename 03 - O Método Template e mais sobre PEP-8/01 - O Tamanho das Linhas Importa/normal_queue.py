from queue import Queue


class NormalQueue(Queue):
    def generate_current_password(self) -> None:
        self.current_password = f"NM{self.code}"

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()
        self.queue.append(self.current_password)

    def call_client(self, cashier: int) -> str:
        current_client = self.queue.pop(0)
        self.customers_served.append(current_client)

        return f"Current Client: {current_client}, go to the cashier: {cashier}"
