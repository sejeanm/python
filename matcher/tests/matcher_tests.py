# Matcher (C) 2023 sejeanm

import unittest

import sys
sys.path.append('../')
from matcher import played_together, load2, get_player_names, get_players_with_not_played, find_matching, find_matching_sure


GRID_FILE = 'input/grid2.csv'
GRID3_FILE = 'input/grid3_empty.csv'
GRID4_FILE = 'input/grid4_half.csv'
GRID5_FILE = 'input/grid5_end.csv'


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")


class TestMatcher(unittest.TestCase):

    @unittest.skip  # no reason needed
    def test_with_whom_played(self):
        p = load2(GRID_FILE)
        # print(json.dumps(p, indent=2))
        print(p)
        self.assertTrue(played_together(p, 'f', 'a'))
        self.assertFalse(played_together(p, 'f', 'f'))
        self.assertFalse(played_together(p, 'f', 'e'))


class TestFunctions(unittest.TestCase):

    @unittest.skip  # no reason needed
    def test_get_player_names(self):
        expected = ['a', 'b', 'c', 'd', 'e', 'f']
        grid = load2(GRID_FILE)
        pl = get_player_names(grid)
        print('All players name: {}'.format(pl))
        self.assertEqual(expected, pl)

    @unittest.skip  # no reason needed
    def test_get_players_with_not_played(self):
        expected = ['a', 'b', 'd', 'e', 'f']
        grid = load2(GRID3_FILE)
        player_name = 'c'
        pl = get_players_with_not_played(grid, player_name)
        print('Player {} did not played with: {}'.format(player_name, pl))
        self.assertEqual(expected, pl)

    def test_find_matching(self):
        # expected = ['a', 'b', 'd', 'e', 'f']
        grid = load2(GRID3_FILE)
        game_proposal = find_matching(grid)
        print('Game proposal: {}'.format(game_proposal))

    def test_find_matching_half(self):
        grid = load2(GRID4_FILE)
        game_proposal = find_matching(grid)
        print('Game proposal for half: {}'.format(game_proposal))

    def test_find_matching_sure(self):
        expected = [['g', 'd'], ['f', 'e'], ['a', 'h'], ['c', 'b']]
        for l in expected:
            l.sort()
        expected.sort()

        grid = load2(GRID5_FILE)
        expected_games = 4
        game_proposal = find_matching_sure(grid, expected_games)
        for l in game_proposal:
            l.sort()
        game_proposal.sort()

        print('Game proposal for end round: {}'.format(game_proposal))
        self.assertListEqual(expected, game_proposal)


if __name__ == '__main__':
    unittest.main()
