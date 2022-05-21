from paper_rock_scissors.players.player import Player
from paper_rock_scissors.symbol import Symbol


class HumanPlayer(Player):

    def play(self) -> Symbol:
        user_input = input("Enter the number for the symbol of this match:"
                           f"{Symbol.PAPER.name}: [{Symbol.PAPER.value}]"
                           f"{Symbol.ROCK.name}: [{Symbol.ROCK.value}]"
                           f"{Symbol.SCISSORS.name}: [{Symbol.SCISSORS.value}]")
        symbol = Symbol(user_input)
        return symbol
