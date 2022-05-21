from paper_rock_scissors.players.player import Player
from paper_rock_scissors.symbol import Symbol


class HumanPlayer(Player):
    def play(self) -> Symbol:
        user_input = input(
            "Enter the number for your move in this match:"
            f"\nFor {Symbol.PAPER.name}: Press [{Symbol.PAPER.value}]"
            f"\nFor {Symbol.ROCK.name}: Press [{Symbol.ROCK.value}]"
            f"\nFor {Symbol.SCISSORS.name}: Press [{Symbol.SCISSORS.value}]: "
        )
        symbol = Symbol(int(user_input))
        return symbol
