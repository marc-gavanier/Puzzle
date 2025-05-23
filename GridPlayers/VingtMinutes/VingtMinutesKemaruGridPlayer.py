﻿from time import sleep

from playwright.sync_api import BrowserContext

from Board.Grid import Grid
from GridPlayers.GridPlayer import GridPlayer
from GridPlayers.PuzzleMobiles.PuzzlesMobileGridPlayer import PuzzlesMobileGridPlayer


class VingtMinutesKemaruGridPlayer(GridPlayer, PuzzlesMobileGridPlayer):
    @classmethod
    def play(cls, grid_solution: Grid, browser: BrowserContext):
        page = browser.pages[0]
        cells = page.query_selector_all("g.grid-cell")
        for position, solution_value in grid_solution:
            index = position.r * grid_solution.columns_number + position.c
            cells[index].click()
            page.keyboard.press(str(solution_value))

        sleep(6)
