from queue import Queue
from constraints import PRIORITY_CODE


class PriorityQueue(Queue):
    def generate_current_password(self) -> None:
        self.current_password = f"{PRIORITY_CODE}{self.code}"

    def call_client(self, cashier: int) -> str:
        current_client = self.queue.pop(0)
        self.customers_served.append(current_client)

        return f"Current Client: {current_client}, go to the cashier: {cashier}"

    def statistic(self, day: str, agency: int, flag: str) -> dict:
        if flag != "detail":
            statistic = {f"{agency}-{day}": len(self.customers_served)}
        else:
            statistic = {
                "day": day,
                "agency": agency,
                "customers_served": self.customers_served,
                "quantity_customers_served": len(self.customers_served)
            }

        return statistic
