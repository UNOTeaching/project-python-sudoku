import unittest

from sudoku_board import Sudoku
from sudoku6 import Context

from .partial_sudokus import DICTS, INITIAL


class TestSudoku(unittest.TestCase):
    def test_sudoku(self):
        for k, d in DICTS.items():
            sudoku = Sudoku(d)
            context = Context(sudoku)
            self.assertEqual(context.initial(), INITIAL[k], k)
