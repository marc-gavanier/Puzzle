﻿# from GridProviders.PuzzleNonogramGridProvider import PuzzleNonogramGridProvider
# from GridProviders.StringGridProvider import StringGridProvider
# from Puzzles.Nonogram.NonogramSolver import NonogramSolver
# from Utils.Board import Board
# 
# 
# class NonogramMainConsole:
#     @staticmethod
#     def main():
#         numbers_by_top_left = NonogramMainConsole.get_grid()
#         NonogramMainConsole.run(numbers_by_top_left)
# 
#     @staticmethod
#     def get_grid():
#         print("Nonogram Game")
#         print("Enter url or grid")
#         console_input = input()
# 
#         url_patterns = {
#             r"https://fr.puzzle-nonograms.com/": PuzzleNonogramGridProvider,
#             r"https://www.puzzle-nonograms.com/": PuzzleNonogramGridProvider
#         }
# 
#         for pattern, provider_class in url_patterns.items():
#             if pattern in console_input:
#                 provider = provider_class()
#                 return provider.get_grid(console_input)
# 
#         return StringGridProvider().get_grid(console_input)
# 
#     @staticmethod
#     def run(numbers_by_top_left):
#         game_solver = NonogramSolver(numbers_by_top_left)
#         solution = game_solver.get_solution()
# 
#         if not solution.is_empty():
#             print(f"Solution found:")
#             print(NonogramMainConsole.get_console_grid(solution))
#         else:
#             print(f"No solution found")
#         # NonogramMainConsole.generate_html(solution_grid)
# 
#     @staticmethod
#     def get_console_grid(solution_grid):
#         background_grid = Board([[1 if solution_grid.value(r, c) else 0 for c in range(solution_grid.columns_number)] for r in range(solution_grid.rows_number)])
#         text_grid = Board([[' ' for _ in range(solution_grid.columns_number)] for _ in range(solution_grid.rows_number)])
#         console_grid = text_grid.to_console_string(None, background_grid)
#         return console_grid
# 
# 
# if __name__ == '__main__':
#     NonogramMainConsole.main()
