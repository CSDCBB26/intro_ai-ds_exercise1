import unittest
from puzzle.heuristics import hamming_distance, manhattan_distance

class TestHeuristics(unittest.TestCase):

    def test_hamming_distance(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.assertEqual(hamming_distance(board), 0)

        board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        self.assertEqual(hamming_distance(board), 2)

        board = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]
        self.assertEqual(hamming_distance(board), 7)

    def test_manhattan_distance(self):
        board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.assertEqual(manhattan_distance(board), 0)

        board = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
        self.assertEqual(manhattan_distance(board), 2)

        board = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]
        self.assertEqual(manhattan_distance(board), 11)

    def test_unsolvable_board(self):
        board = [[1, 2, 3], [4, 5, 6], [8, 7, 0]]
        self.assertEqual(hamming_distance(board), 2)
        self.assertEqual(manhattan_distance(board), 2)

    def test_null_values(self):
        with self.assertRaises(TypeError):
            hamming_distance(None)
        with self.assertRaises(TypeError):
            manhattan_distance(None)

    def test_false_values(self):
        with self.assertRaises(TypeError):
            hamming_distance(False)
        with self.assertRaises(TypeError):
            manhattan_distance(False)

if __name__ == '__main__':
    unittest.main()