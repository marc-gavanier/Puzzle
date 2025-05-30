﻿import math
from typing import List, Tuple

from Domain.Board.Grid import Grid
from Domain.Board.Position import Position
from Domain.Ports.SolverEngine import SolverEngine
from Domain.Puzzles.GameSolver import GameSolver


class KenKenSolver(GameSolver):
    def __init__(self, regions_operators_results: List[Tuple[List[Position], str, int]], solver_engine: SolverEngine):
        self._regions_operators_results = regions_operators_results
        self.rows_number, self.columns_number = self._get_rows_columns_number()
        if self.rows_number != self.columns_number:
            raise ValueError("KenKen grid must be square")
        self._grid_z3 = None
        self._solver = solver_engine
        self._previous_solution: Grid | None = None

    def get_solution(self) -> (Grid | None, int):
        self._grid_z3 = Grid([[self._solver.int(f"grid_{r}_{c}") for c in range(self.columns_number)] for r in range(self.rows_number)])
        if self._add_constraints() is False:
            return Grid.empty()
        self._previous_solution = Grid([[self._solver.eval(self._grid_z3.value(i, j)) for j in range(self.columns_number)] for i in range(self.rows_number)])
        return self._previous_solution

    def get_other_solution(self):
        constraints = []
        for position, value in self._previous_solution:
            constraints.append(self._grid_z3[position] == value)
        self._solver.add(self._solver.Not(self._solver.And(constraints)))
        return self.get_solution()

    def _add_constraints(self):
        self._initials_constraints()
        self._add_distinct_in_rows_and_columns_constraints()
        self._add_operations_add_constraints()
        self._add_operations_sub_constraints()
        if not self._solver.has_solution():
            return False
        self._add_operations_mul_constraints()
        self._add_operations_div_constraints()
        if not self._solver.has_solution():
            return False
        return True

    def _initials_constraints(self):
        for position, value in self._grid_z3:
            self._solver.add(self._grid_z3[position] >= 1)
            self._solver.add(self._grid_z3[position] <= self.rows_number)

    def _add_distinct_in_rows_and_columns_constraints(self):
        for r in range(self.rows_number):
            self._solver.add(self._solver.distinct([self._grid_z3[Position(r, c)] for c in range(self.columns_number)]))
        for c in range(self.columns_number):
            self._solver.add(self._solver.distinct([self._grid_z3[Position(r, c)] for r in range(self.rows_number)]))

    def _add_operations_mul_constraints(self):
        for region, _, result in [(region, operator_str, result) for region, operator_str, result in self._regions_operators_results if operator_str == 'x']:
            constraint = math.prod([self._grid_z3[position] for position in region]) == result
            self._solver.add(constraint)

    def _add_operations_div_constraints(self):
        for region, _, result in [(region, operator_str, result) for region, operator_str, result in self._regions_operators_results if operator_str == '÷']:
            if len(region) != 2:
                raise ValueError("Division can only be applied to two positions")
            constraint = self._solver.Or(
                self._grid_z3[region[0]] * result == self._grid_z3[region[1]],
                self._grid_z3[region[1]] * result == self._grid_z3[region[0]]
            )
            self._solver.add(constraint)

    def _add_operations_add_constraints(self):
        for region, _, result in [(region, operator_str, result) for region, operator_str, result in self._regions_operators_results if operator_str == '+']:
            constraint = sum([self._grid_z3[position] for position in region]) == result
            self._solver.add(constraint)

    def _add_operations_sub_constraints(self):
        for region, _, result in [(region, operator_str, result) for region, operator_str, result in self._regions_operators_results if operator_str == '-']:
            if len(region) != 2:
                raise ValueError("Subtraction can only be applied to two positions")
            constraint = self._solver.abs(self._grid_z3[region[0]] - self._grid_z3[region[1]]) == result
            self._solver.add(constraint)

    def _get_rows_columns_number(self) -> (int, int):
        all_positions = [pos for sublist, _, _ in self._regions_operators_results for pos in sublist]
        min_r = min(pos.r for pos in all_positions)
        max_r = max(pos.r for pos in all_positions)
        min_c = min(pos.c for pos in all_positions)
        max_c = max(pos.c for pos in all_positions)
        return max_r - min_r + 1, max_c - min_c + 1
