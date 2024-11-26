import unittest
from astar import Node, heuristic, astar_search

class TestAStarSearch(unittest.TestCase):

    def setUp(self):
        self.grid = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0]
        ]
        self.start = (0, 0)
        self.goal = (4, 4)

    def test_heuristic(self):
        self.assertEqual(heuristic((0, 0), (4, 4)), 8)
        self.assertEqual(heuristic((1, 1), (4, 4)), 6)
        self.assertEqual(heuristic((2, 2), (4, 4)), 4)

    def test_astar_search(self):
        path = astar_search(self.start, self.goal, self.grid)
        expected_path = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]
        self.assertEqual(path, expected_path)

    def test_no_path(self):
        grid = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        start = (0, 0)
        goal = (2, 2)
        path = astar_search(start, goal, grid)
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()