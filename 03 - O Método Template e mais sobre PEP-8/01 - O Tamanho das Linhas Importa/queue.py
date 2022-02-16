class Queue:
    code: int = 0
    queue = []
    customers_served = []
    current_password: str = ""

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1
