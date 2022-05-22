from paper_rock_scissors.game import Game
from paper_rock_scissors.players.cpu_player import CPUPlayer
from paper_rock_scissors.players.human_player import HumanPlayer

if __name__ == "__main__":
    print("Welcome to Paper Rock Scissors console edition!")
    try:
        num_of_matches = int(input("Enter the total number of matches you desire to play in this Game: "))
        print(f"Great, you are playing {num_of_matches} matches")
    except ValueError:
        print("Oops! That was not a valid number. Try again...")
        raise

    player_name = input("Now, input player's name to start: ")

    human_player = HumanPlayer(player_name)
    cpu_player = CPUPlayer()
    game = Game(human_player, cpu_player, num_of_matches)
    game.start_game()
