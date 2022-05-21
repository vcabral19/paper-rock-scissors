from random import randint

from paper_rock_scissors.players.player import Player
from paper_rock_scissors.symbol import Symbol


class CPUPlayer(Player):
    def __init__(self):
        super().__init__("CPU Player")

    def play(self) -> Symbol:
        print(f"{self.name} is carefully considering his move")
        symbol = Symbol(randint(0, len(Symbol) - 1))
        return symbol
