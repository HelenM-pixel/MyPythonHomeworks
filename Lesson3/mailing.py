from addresses import Address


class Mailing:
    def __init__(self, track: str, from_address: Address,
                 to_address: Address, cost: float):
        self.track = track
        self.from_address = from_address
        self.to_address = to_address
        self.cost = cost

    def __str__(self):
        return (f"{self.track} из: {self.from_address}, "
                f"в {self.to_address}. Стоимость: {self.cost}")
