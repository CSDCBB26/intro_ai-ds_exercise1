import unittest

from puzzle.board import Board


class TestBoard(unittest.TestCase):

    def test_default_board(self):
        board = Board()
        expected_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.assertEqual(board.board, expected_board)

    def test_custom_board(self):
        custom_board = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]
        board = Board(custom_board)
        self.assertEqual(board.board, custom_board)

    def test_is_solvable(self):
        solvable_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        unsolvable_board = [1, 2, 3, 4, 5, 6, 8, 7, 0]
        self.assertTrue(Board.is_solvable(solvable_board))
        self.assertFalse(Board.is_solvable(unsolvable_board))

    def test_generate_random(self):
        board = Board.generate_random()
        flattened_board = [tile for row in board.board for tile in row]
        self.assertTrue(Board.is_solvable(flattened_board))

    def test_str_representation(self):
        board = Board()
        expected_str = "1 2 3\n4 5 6\n7 8 0"
        self.assertEqual(str(board), expected_str)


if __name__ == '__main__':
    unittest.main()
