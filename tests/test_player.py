import unittest
from unittest import mock

from paper_rock_scissors.players.player import Player


class PlayerTestCase(unittest.TestCase):
    @mock.patch.multiple(Player, __abstractmethods__=set())
    def test_win(self):
        player_instance = Player("mocked_player")

        self.assertEqual(player_instance.victories, 0)

        player_instance.win()

        self.assertEqual(player_instance.victories, 1)
