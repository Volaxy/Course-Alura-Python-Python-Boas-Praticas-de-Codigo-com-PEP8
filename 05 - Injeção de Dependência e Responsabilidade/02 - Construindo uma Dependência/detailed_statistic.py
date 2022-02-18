from typing import List


class DetailedStatistic:
    def __init__(self, day: str, agency: int) -> None:
        self.day = day
        self.agency = agency

    def run_statistic(self, clients_served: List[str]) -> dict:
        statistic = {
            "day": self.day,
            "agency": self.agency,
            "customers_served": self.customers_served,
            "quantity_customers_served": len(self.customers_served)
        }
