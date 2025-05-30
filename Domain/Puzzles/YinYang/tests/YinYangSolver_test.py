﻿import unittest
from unittest import TestCase

from Domain.Board.Grid import Grid
from Domain.Puzzles.YinYang.YinYangSolver import YinYangSolver
from SolverEngineAdapters.Z3SolverEngine import Z3SolverEngine

_ = ''


class YinYangSolverTests(TestCase):
    @staticmethod
    def get_solver_engine():
        return Z3SolverEngine()

    def test_solution_square_constraint(self):
        grid = Grid([
            [1, 1, 1, 1, 1, 1],
            [1, _, 0, 0, 0, 0],
            [1, 1, 1, _, _, 0],
            [1, _, 1, 1, 1, 0],
            [1, 0, _, _, _, 0],
            [1, 0, 0, 0, 0, 0],
        ])
        expected_grid = Grid([
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_square_diagonal_constraint(self):
        grid = Grid([
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, _],
            [1, 0, 1, 1, 1, _],
            [1, 0, _, _, _, _],
            [1, 0, _, _, _, _],
        ])
        expected_grid = Grid([
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_6x6_easy(self):
        grid = Grid([
            [_, _, _, _, _, 1],
            [_, _, 0, _, 0, 0],
            [_, 1, _, _, _, _],
            [_, _, 1, 1, _, _],
            [_, 0, _, _, _, _],
            [1, 0, _, _, _, _],
        ])
        expected_grid = Grid([
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_6x6_normal(self):
        grid = Grid([
            [_, _, _, 1, _, 0],
            [1, _, _, _, _, _],
            [_, 1, _, 1, _, _],
            [_, 0, _, _, 1, _],
            [_, 0, 0, _, 1, _],
            [_, _, _, _, _, _],
        ])
        expected_grid = Grid([
            [1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [1, 0, 0, 0, 1, 0],
            [1, 1, 1, 0, 0, 0]
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_6x6_hard(self):
        grid = Grid([
            [_, _, 1, _, _, 1],
            [1, _, _, 1, _, _],
            [_, 0, _, _, _, _],
            [_, _, _, _, 0, _],
            [_, _, 1, 0, 0, _],
            [_, _, _, _, _, _],
        ])
        expected_grid = Grid([
            [1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_10x10_hard(self):
        grid = Grid([
            [_, _, _, _, _, 1, _, 0, _, _],
            [_, _, 1, _, _, _, _, 0, _, _],
            [_, _, _, 0, _, _, 0, _, _, _],
            [_, _, 0, _, 0, _, _, _, _, _],
            [_, _, _, 0, _, 0, 0, 1, _, _],
            [_, _, 1, _, _, 0, _, _, _, _],
            [_, 1, _, 1, _, 0, _, _, 0, _],
            [_, _, _, _, _, _, _, 0, _, _],
            [_, _, 1, _, 1, 0, _, 1, _, _],
            [_, _, _, 1, _, _, _, _, _, _],
        ])
        expected_grid = Grid([
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_15x15_easy(self):
        grid = Grid([
            [_, _, _, _, _, _, 0, _, 1, _, _, _, _, _, _],
            [0, _, _, 0, _, 0, _, 1, _, _, _, _, _, _, _],
            [_, _, 1, _, 1, _, 0, 0, 0, _, 0, _, 0, _, _],
            [_, 0, _, _, _, 0, _, 1, _, _, _, 1, _, _, _],
            [_, _, _, 1, _, _, 0, _, _, 1, _, _, _, 1, _],
            [_, 0, _, _, _, 0, _, 1, _, 0, _, 0, _, _, _],
            [_, _, _, 1, _, _, 0, 0, _, _, _, _, 0, _, _],
            [_, _, 0, _, _, 0, _, _, 0, _, 0, _, _, _, _],
            [_, _, 0, _, 1, 0, 1, 0, 0, 1, _, _, _, 1, _],
            [_, 0, 1, 1, _, 0, _, _, 0, _, _, _, _, _, _],
            [_, 0, 1, _, 0, _, 1, _, _, _, _, _, 0, _, _],
            [_, 0, 1, 0, _, 0, 1, 0, _, _, _, 1, _, _, _],
            [_, 0, 1, 0, 1, 0, 1, 0, 1, 0, _, _, 0, _, _],
            [_, _, 1, _, 1, _, 1, _, 1, _, _, 1, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
        ])
        expected_grid = Grid([
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    def test_solution_15x15_hard(self):
        grid = Grid([
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [_, _, _, 1, 1, 1, 1, 1, _, 1, 1, _, 1, _, _],
            [_, 0, _, 0, _, _, _, _, 1, _, _, 1, _, 1, _],
            [_, _, 0, _, _, 1, 1, 1, _, _, 1, _, _, 1, _],
            [_, _, _, 0, 0, 0, 0, 0, _, _, _, 1, _, 1, _],
            [_, _, _, _, _, _, _, 1, _, _, 0, 1, _, 1, _],
            [_, 0, _, 0, _, 0, _, _, _, _, _, 1, _, 1, _],
            [_, _, _, 0, _, 0, _, 0, _, 0, _, _, _, 1, _],
            [_, _, 0, _, _, 0, _, 0, _, _, _, 1, _, 1, _],
            [_, _, 0, _, _, 0, _, 0, _, 0, _, _, _, 1, _],
            [_, _, _, 0, _, _, 0, _, _, _, _, 1, _, 1, _],
            [_, 0, _, _, _, _, 1, _, _, _, 0, _, _, _, _],
            [_, _, _, _, 1, _, _, _, _, _, 0, _, 0, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
        ])
        expected_grid = Grid([
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    # @unittest.skip("20 sec")
    def test_solution_20x20_normal(self):
        grid = Grid([
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, 1, _, _, 0, _, _, _, _, _, 0, _, 0, _, 0, _, _, _, _, _],
            [_, _, _, _, _, 1, _, 1, _, _, _, _, _, _, _, _, 0, 0, 0, _],
            [_, 1, 1, _, 1, _, 1, _, _, 0, _, _, 1, _, 1, _, _, _, _, _],
            [_, _, 0, _, _, _, _, 1, 0, 0, _, _, 1, _, 0, 0, 0, 0, 0, _],
            [_, 0, _, 0, 1, _, _, _, _, 0, 1, _, _, _, _, _, _, _, _, _],
            [_, 0, _, 0, 1, _, 1, _, 0, _, _, _, 0, _, _, _, 0, _, 0, _],
            [_, 0, _, 0, 1, _, 1, 0, _, _, 1, 0, 0, 1, _, _, _, 0, _, _],
            [_, 0, _, 0, _, 1, _, 0, _, 1, _, _, _, _, _, 0, _, _, _, _],
            [_, 0, _, _, _, _, 1, _, _, 0, _, 0, _, 0, 0, _, 1, _, 1, _],
            [_, _, _, _, 1, _, 1, _, _, 1, _, _, _, _, 1, _, _, 1, _, _],
            [_, _, 1, _, 1, _, 1, _, 1, _, _, 1, _, 1, _, _, 0, 0, 0, _],
            [_, _, 1, _, _, 1, _, 1, _, 1, 1, _, _, _, _, _, _, 1, _, _],
            [_, _, 1, _, 1, _, _, _, _, _, 0, _, _, _, 1, 0, _, _, _, _],
            [_, _, 1, _, _, 1, 1, 1, 1, _, _, _, 0, _, _, _, 0, _, 0, _],
            [_, _, 1, _, 1, _, _, _, _, _, 0, _, _, 1, _, _, _, _, _, _],
            [_, 1, _, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, _, 0, _, 0, _],
            [_, _, _, _, 0, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, 1, _, _, _, 1, _, 1, 1, 1, 1, 1, 1, _, _, _, 1, _, _],
            [_, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, _, _]
        ])
        expected_grid = Grid([
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    @unittest.skip("18 sec")
    def test_solution_20x20_hard(self):
        grid = Grid([
            [_, _, _, _, _, _, _, _, _, _, _, _, _, 0, _, _, _, _, _, _],
            [_, _, _, 1, _, 0, _, _, _, _, _, 1, 1, _, _, _, _, 0, _, _],
            [_, 0, _, _, 1, _, 0, 0, 0, 0, _, _, _, 1, _, 0, _, _, _, _],
            [_, _, _, 1, _, _, _, _, _, _, _, 1, 1, _, 0, _, 1, _, 0, _],
            [_, 0, 0, _, 0, _, 0, _, 0, _, 0, _, 0, _, _, _, _, _, 0, _],
            [_, _, _, _, _, _, _, 0, _, _, _, _, _, _, _, _, 0, _, 0, _],
            [_, _, 1, 1, _, 1, _, _, _, 1, _, 1, _, 1, _, _, _, 0, _, _],
            [_, _, 1, _, _, _, _, 0, _, _, _, _, _, _, _, 1, _, 0, _, _],
            [_, _, 0, _, _, _, 0, _, 0, _, 0, _, _, 0, _, _, _, _, _, _],
            [_, _, 0, _, _, 0, _, _, _, _, _, 1, _, 0, _, 0, _, _, 0, _],
            [_, 0, _, 0, 0, _, 0, 0, 0, _, 1, _, 1, 0, _, _, _, _, 0, _],
            [_, _, _, _, _, _, _, _, 1, _, _, _, 1, 0, _, _, 0, _, 0, _],
            [_, _, _, 0, 0, 0, _, 1, _, 1, _, _, 1, 0, _, 0, _, 0, _, _],
            [_, _, 0, _, _, _, _, _, _, _, 1, _, 1, 0, _, _, 1, _, 0, _],
            [_, _, _, 0, 0, 0, _, 1, _, 1, _, _, 1, _, 0, _, _, _, 0, _],
            [_, 0, _, _, _, _, _, _, _, _, 1, _, _, 0, _, _, 0, _, 0, _],
            [_, _, _, _, _, 0, _, 0, _, _, _, _, _, _, _, _, 0, _, 0, _],
            [_, _, _, 0, _, _, _, _, 0, _, 0, _, _, _, 0, _, 0, _, 0, _],
            [_, _, 0, _, _, _, _, _, 0, _, 0, _, _, _, 0, _, 0, _, 0, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 0, 1]
        ])
        expected_grid = Grid([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    @unittest.skip("2mn45")
    def test_solution_25x25_hard(self):
        grid = Grid([
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 0, _, _, _, _, _, _, _],
            [_, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 0, _, _, 0, 0, 0, _, _, 1, _],
            [_, 0, 0, _, _, _, _, _, _, _, _, _, _, _, 1, 0, _, 0, _, _, 1, 1, _, _, _],
            [_, _, _, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _, 1, _, _, _, _, _],
            [_, 0, _, 0, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, 1, _, 1, _, 1, _, _],
            [_, _, _, 0, _, 1, 1, 1, 1, 1, 1, 1, _, 1, _, _, 1, _, _, 1, _, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, 0, 1, _, _, _, 1, _, _, _, _, _, _, 1, _],
            [_, 0, _, _, _, 1, 1, 1, 1, 1, _, _, _, 0, _, _, 1, _, 1, _, 0, 0, 1, 1, _],
            [_, _, 1, _, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, _, _, _, _, _, _, 1, _],
            [_, 1, _, _, _, 1, 1, 1, 1, _, _, _, _, 1, _, 1, _, _, _, _, _, _, 0, 1, _],
            [_, _, _, _, 1, _, _, _, _, 1, _, _, 1, _, _, _, _, _, _, 1, _, _, _, 1, _],
            [_, _, 1, _, _, _, 1, 1, 1, _, _, 1, _, _, _, _, _, _, 0, _, 1, _, 0, 1, _],
            [_, _, _, _, _, _, _, 1, _, 1, _, _, 1, 0, _, 0, 1, _, _, 0, _, 0, _, 1, _],
            [_, 0, _, 0, _, _, _, _, _, _, _, _, _, 0, _, 0, _, _, 0, _, _, _, 0, 1, _],
            [_, _, _, _, _, _, _, _, 1, 1, 1, _, _, _, 0, _, _, 1, _, 0, 1, _, _, 1, _],
            [_, _, _, 0, _, 0, _, 0, _, 0, _, _, 1, 1, _, _, 1, _, _, 0, _, 0, _, _, _],
            [_, 0, _, _, 0, _, _, _, _, _, _, 1, _, _, 1, _, _, 1, _, _, _, _, _, 1, _],
            [_, _, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, _, 0, _, _, 0, _, 0, _, _, _],
            [_, 0, 0, 0, _, 1, _, _, _, _, _, 1, _, _, 0, 0, _, 1, _, _, _, _, _, 1, _],
            [_, _, _, 0, _, _, _, 0, _, 0, _, _, _, _, _, _, 0, _, 1, _, _, _, 1, _, _],
            [_, _, _, 1, _, _, _, _, 0, _, 1, _, 0, _, 0, 0, _, 1, _, 1, _, 1, _, 1, _],
            [_, _, _, _, _, _, _, 1, 1, 1, _, 0, _, _, _, _, 0, 1, _, 1, _, 1, _, _, _],
            [_, 0, _, _, 0, _, _, _, _, _, 1, 0, 1, _, 1, _, _, 1, _, 1, _, 1, 0, _, _],
            [_, _, _, 0, _, _, 0, _, 1, 1, _, 0, _, _, _, _, 0, _, _, _, _, _, 0, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
        ])
        expected_grid = Grid([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)

    @unittest.skip("40mn")
    def test_solution_30x30(self):
        grid = Grid([
            [_, 0, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
            [_, _, _, 0, _, 0, _, 0, _, 0, _, 0, _, 0, _, 0, _, _, _, _, _, _, _, _, _, 1, _, _, _, _],
            [_, _, 0, _, _, _, 0, _, _, _, 0, _, 0, _, _, _, 0, _, 1, 1, 1, 1, 1, 1, 1, _, _, _, _, _],
            [_, _, _, _, 1, 1, _, _, 1, 1, _, _, _, _, 1, _, _, _, _, _, 0, 0, _, _, _, _, 1, 0, _, _],
            [_, _, _, 0, _, _, 0, _, _, _, 0, _, 0, 1, 0, _, 1, 1, 1, _, 0, _, _, _, 1, _, _, _, _, _],
            [_, 0, _, _, _, 0, _, 0, _, 0, _, 0, _, _, _, _, _, _, _, _, 1, _, 1, _, _, _, _, _, 1, _],
            [_, _, _, _, _, _, _, _, _, _, _, 1, 1, _, _, _, 1, _, _, _, _, _, _, _, _, 0, _, _, _, _],
            [_, 0, 0, _, 0, 0, 0, 0, 0, 0, _, _, _, 1, _, 1, _, 1, 1, _, 0, _, 1, _, _, 0, _, _, _, _],
            [_, _, _, 0, _, _, 1, _, 1, _, 1, _, 1, _, 1, _, _, _, _, _, 1, _, _, _, 1, _, 1, _, 1, _],
            [_, 0, _, _, 0, _, _, 1, _, _, _, 1, _, 1, _, _, _, 0, _, _, _, _, _, 1, _, _, _, 1, _, _],
            [_, _, _, _, _, _, 1, _, _, 0, _, 1, _, _, _, _, 1, 1, 1, 1, 1, 1, _, _, _, _, 1, _, _, _],
            [_, _, _, 0, _, _, _, _, 0, _, _, _, _, 1, 1, _, _, 0, 0, 0, _, _, _, _, _, _, _, 1, _, _],
            [_, 0, _, _, _, 0, _, 0, _, 0, 0, 0, _, 0, 0, 0, _, _, _, _, _, 0, _, _, 0, _, _, _, _, _],
            [_, _, 1, _, _, _, _, _, 1, 1, 1, _, 1, _, 1, _, _, 0, _, 1, _, _, 1, 1, _, 0, _, 1, _, _],
            [_, 1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1, _, 1, _, 0, _, _, _, 0, _, _, _, _],
            [_, _, _, _, 1, _, 1, _, _, 0, _, 0, _, 0, _, _, 1, _, 1, _, 1, 0, _, 0, _, 0, 1, _, _, _],
            [_, _, 1, 1, _, _, _, 0, 1, _, _, _, _, 1, _, 1, _, _, 1, _, _, _, _, _, _, _, _, 1, _, _],
            [_, _, _, _, _, _, _, _, _, 0, _, 0, _, _, 1, _, 1, _, _, 1, _, 0, _, 1, 0, _, _, _, _, _],
            [_, _, 1, 1, 1, _, _, _, _, _, 0, _, _, 1, _, _, _, _, 1, _, 1, 0, 0, _, _, _, _, _, 0, _],
            [_, _, _, 0, _, _, 1, _, 1, _, _, 0, _, _, _, 1, 1, _, _, _, _, 0, _, _, _, _, 1, _, _, _],
            [_, 1, _, _, _, _, _, _, _, 1, _, _, 1, 1, _, _, 0, _, 0, _, _, 0, 1, 1, _, 1, _, 1, _, _],
            [_, _, _, _, 1, _, 1, 1, 1, _, 1, _, _, _, _, _, _, _, _, _, 0, _, _, 1, _, _, 1, _, _, _],
            [_, _, 1, 0, 0, _, _, _, _, 1, _, _, _, _, 1, 0, 1, _, 0, _, _, 1, _, _, _, _, _, 1, _, _],
            [_, _, _, 0, _, _, 0, _, 1, _, _, _, 1, _, 1, 0, _, _, _, _, _, _, 1, _, 1, _, 1, _, 0, _],
            [_, _, _, _, _, _, 0, _, _, _, 0, _, _, _, 1, 0, _, 0, 0, _, _, 1, _, _, 1, _, _, _, 0, _],
            [_, 0, _, _, _, 0, _, _, 0, _, _, 0, _, _, _, 0, _, _, _, _, 0, 0, _, _, _, _, 1, _, _, _],
            [_, _, 1, _, 1, 1, _, _, 0, _, 0, _, _, 0, _, 0, _, 0, _, 0, _, 1, _, _, 0, _, _, 1, _, _],
            [_, _, _, _, _, _, 1, _, _, _, _, _, 1, 0, _, 0, _, 0, _, 0, _, _, 1, 1, _, 0, 1, _, 1, _],
            [_, _, 1, 1, 1, 1, _, 0, _, _, 0, _, _, 0, _, 0, _, 0, _, 0, _, 0, _, _, _, 0, _, _, _, _],
            [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _]
        ])
        expected_grid = Grid([
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        game_solver = YinYangSolver(grid, self.get_solver_engine())
        solution = game_solver.get_solution()
        self.assertEqual(expected_grid, solution)
        other_solution = game_solver.get_other_solution()
        self.assertEqual(Grid.empty(), other_solution)


if __name__ == '__main__':
    unittest.main()
