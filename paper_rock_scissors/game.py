from time import sleep

from paper_rock_scissors.players.player import Player
from paper_rock_scissors.symbol import Symbol


class Game:
    victory_rules = {
        Symbol.PAPER: {Symbol.ROCK: True, Symbol.SCISSORS: False},
        Symbol.ROCK: {Symbol.SCISSORS: True, Symbol.PAPER: False},
        Symbol.SCISSORS: {Symbol.PAPER: True, Symbol.ROCK: False},
    }

    def __init__(self, player1: Player, player2: Player, num_matches: int):
        self.player1 = player1
        self.player2 = player2
        self.num_matches = num_matches

    def _player1_wins(self, symbol_player1: Symbol, symbol_player2: Symbol) -> bool:
        symbol1_rule = self.victory_rules.get(symbol_player1)
        if symbol1_rule is None:
            raise TypeError
        victory = symbol1_rule.get(symbol_player2)
        if victory is None:
            raise TypeError
        return victory

    def _play_match(self, symbol_player1: Symbol, symbol_player2: Symbol) -> str:
        if symbol_player1 == symbol_player2:
            return f"Draw! Both players used {symbol_player1.name}"
        if self._player1_wins(symbol_player1, symbol_player2):
            self.player1.win()
            return f"This match goes for {self.player1.name}! {symbol_player1.name} beats {symbol_player2.name}"
        else:
            self.player2.win()
            return f"This match goes for {self.player2.name}! {symbol_player2.name} beats {symbol_player1.name}"

    def _broadcast_winner(self) -> str:
        print("... and the winner is ")
        sleep(1)
        print("... ")
        sleep(1)
        print("... ")
        sleep(1)
        print("... ")
        if self.player1.victories > self.player2.victories:
            announcement = f"{self.player1.name} with {self.player1.victories} victories! Congratulations!!"
        elif self.player2.victories > self.player1.victories:
            announcement = f"{self.player2.name} with {self.player2.victories} victories! Congratulations!!"
        else:
            announcement = (
                f"Both {self.player1.name} and {self.player2.name} have {self.player1.victories} victories. That's "
                "a TIED GAME!"
            )
        return announcement

    def start_game(self) -> None:
        print("Starting the game")
        for i in range(self.num_matches):
            print(f"Match number {i + 1}")
            print(self._play_match(self.player1.play(), self.player2.play()))
            print("End of the Match!")
            print("----------------------------------------")

        print(self._broadcast_winner())
        print("Game Over")
