import unittest
from unittest import mock

from paper_rock_scissors.game import Game
from paper_rock_scissors.symbol import Symbol


class GameTestCase(unittest.TestCase):
    player1 = mock.Mock()
    player2 = mock.Mock()

    @staticmethod
    def mock_player1_win(symbol_player1, symbol_player2):
        return True

    @staticmethod
    def mock_play_match(symbol_player1, symbol_player2):
        return "match winner"

    @staticmethod
    def mock_broadcast_winner():
        return "final winner"

    def test_rock_beats_scissors(self):
        game = Game(self.player1, self.player2, 1)

        symbol_player1 = Symbol.ROCK
        symbol_player2 = Symbol.SCISSORS

        assert game._player1_wins(symbol_player1, symbol_player2)

    def test_scissors_beats_paper(self):
        game = Game(self.player1, self.player2, 1)

        symbol_player1 = Symbol.SCISSORS
        symbol_player2 = Symbol.PAPER

        assert game._player1_wins(symbol_player1, symbol_player2)

    def test_paper_beats_rock(self):
        game = Game(self.player1, self.player2, 1)

        symbol_player1 = Symbol.PAPER
        symbol_player2 = Symbol.ROCK

        assert game._player1_wins(symbol_player1, symbol_player2)

    def test_play_match_draw(self):
        game = Game(self.player1, self.player2, 1)

        match_result = game._play_match(Symbol.ROCK, Symbol.ROCK)

        self.assertTrue(match_result.startswith("Draw"))
        self.assertEqual(self.player1.call_count, 0)
        self.assertEqual(self.player2.call_count, 0)

    @mock.patch("paper_rock_scissors.game.Game._player1_wins", side_effect=mock_player1_win)
    def test_player1_win(self, player1_win_mock):
        symbol1 = mock.Mock()
        symbol2 = mock.Mock()

        player1 = mock.Mock()
        player2 = mock.Mock()

        Game._player1_wins = player1_win_mock

        game = Game(player1, player2, 1)
        game._play_match(symbol1, symbol2)

        self.assertEqual(player1.win.call_count, 1)
        self.assertEqual(player2.win.call_count, 0)

    @mock.patch("paper_rock_scissors.game.Game._player1_wins", side_effect=mock_player1_win)
    def test_broadcast_winner(self, player1_win_mock):
        symbol1 = mock.Mock()
        symbol2 = mock.Mock()

        player1 = self.player1
        player2 = self.player2

        player1.victories = 2
        player2.victories = 1

        player1.name = "player1"

        game = Game(player1, player2, 1)

        game._play_match(symbol1, symbol2)

        self.assertTrue(game._broadcast_winner().startswith(self.player1.name))

    @mock.patch("paper_rock_scissors.game.Game._play_match", side_effect=mock_play_match)
    @mock.patch("paper_rock_scissors.game.Game._broadcast_winner", side_effect=mock_broadcast_winner)
    def test_number_of_matches_equals_n(self, _broadcast_winner_mock, _play_match_mock):
        expected_n_matches = 6

        game = Game(self.player1, self.player2, expected_n_matches)
        game.start_game()

        self.assertEqual(_play_match_mock.call_count, 6)
        self.assertEqual(_broadcast_winner_mock.call_count, 1)
