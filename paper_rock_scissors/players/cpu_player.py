from paper_rock_scissors.players.player import Player
from paper_rock_scissors.symbol import Symbol


class CPUPlayer(Player):

    def __init__(self):
        super().__init__("CPU Player")

    def play(self) -> Symbol:
        pass
