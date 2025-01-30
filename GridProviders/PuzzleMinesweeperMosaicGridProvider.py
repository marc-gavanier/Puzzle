﻿import math

from playwright.sync_api import BrowserContext

from GridProviders.GridProvider import GridProvider
from GridProviders.PlaywrightGridProvider import PlaywrightGridProvider
from GridProviders.PuzzlesMobileGridProvider import PuzzlesMobileGridProvider
from Utils.Grid import Grid


class PuzzleMinesweeperMosaicGridProvider(GridProvider, PlaywrightGridProvider, PuzzlesMobileGridProvider):
    def get_grid(self, url: str):
        return self.with_playwright(self.scrap_grid, url)

    def scrap_grid(self, browser: BrowserContext, url):
        page = browser.pages[0]
        page.goto(url)
        self.new_game(page, 'div.cell')
        numbers_divs = page.query_selector_all('div.number')
        numbers = [int(inner_text) if (inner_text := number_div.inner_text()) else -1 for number_div in numbers_divs]
        cells_count = len(numbers)
        side = int(math.sqrt(cells_count))
        matrix = []
        for i in range(0, cells_count, side):
            matrix.append(numbers[i:i + side])
        return Grid(matrix)
