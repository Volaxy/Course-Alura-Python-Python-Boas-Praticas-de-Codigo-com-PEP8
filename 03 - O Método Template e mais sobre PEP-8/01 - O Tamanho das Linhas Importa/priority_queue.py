from queue import Queue


class PriorityQueue(Queue):
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

    def statistic(self, day: str, agency: int, flag: str) -> dict:
        if flag != "detail":
            statistic = {f"{agency}-{day}": len(self.customers_served)}
        else:
            statistic = {}
            statistic["day"] = day
            statistic["agency"] = agency
            statistic["customers_served"] = self.customers_served
            statistic["quantity_customers_served"] = len(self.customers_served)

        return statistic
