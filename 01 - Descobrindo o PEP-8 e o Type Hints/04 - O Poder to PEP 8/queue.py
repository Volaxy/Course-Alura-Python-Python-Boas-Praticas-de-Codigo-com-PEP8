class NormalQueue:
    code: int = 0
    queue = []
    customers_served = []
    current_password: str = ""

    def generate_current_password(self) -> None:
        self.current_password = f"NM{self.code}"

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()
        self.queue.append(self.current_password)

    def call_client(self, cashier: int) -> str:
        current_client = self.queue.pop(0)
        self.customers_served.append(current_client)

        return f"Current Client: {current_client}, go to the cashier: {cashier}"
