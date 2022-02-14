class NormalQueue:
    # The "Type Hint" it's the typing of variable to indicates to the programmer the variable type
    code: int = 0
    queue = []
    customers_served = []
    current_password: str = ""

    # The "->" indicates the return type for this function
    def generate_current_password(self) -> None:
        self.current_password = f"NM{self.code}"
