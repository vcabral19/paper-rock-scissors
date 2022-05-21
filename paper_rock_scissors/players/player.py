from abc import ABC, abstractmethod
from paper_rock_scissors.symbol import Symbol


class Player(ABC):
    victories: int

    def __init__(self, player_name: str):
        self.victories = 0
        self.name = player_name
        super().__init__()

    def win(self) -> None:
        self.victories += 1

    @abstractmethod
    def play(self) -> Symbol:
        pass
