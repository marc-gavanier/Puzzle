﻿from bs4 import BeautifulSoup
from playwright.sync_api import BrowserContext

from GridProviders.GridProvider import GridProvider
from GridProviders.PlaywrightGridProvider import PlaywrightGridProvider
from GridProviders.PuzzlesMobile.PuzzlesMobileGridProvider import PuzzlesMobileGridProvider
from Domain.Grid.Grid import Grid
from Domain.Island import Island
from Domain.Position import Position


class PuzzleHashiGridProvider(GridProvider, PlaywrightGridProvider, PuzzlesMobileGridProvider):
    def get_grid(self, url: str):
        return self.with_playwright(self.scrap_grid, url)

    def scrap_grid(self, browser: BrowserContext, url):
        page = browser.pages[0]
        page.goto(url)
        self.new_game(page, 'div.bridges-task-cell')
        html_page = page.content()
        soup = BeautifulSoup(html_page, 'html.parser')
        cell_divs = soup.find_all('div', class_='bridges-task-cell')
        gap_between_cells = 2
        islands = {}
        for cell in cell_divs:
            cell_top = int(cell['style'].split('top: ')[1].split('px')[0])
            cell_left = int(cell['style'].split('left: ')[1].split('px')[0])
            cell_width = int(cell['style'].split('width: ')[1].split('px')[0])
            cell_height = int(cell['style'].split('height: ')[1].split('px')[0])
            row = cell_top // (cell_height + gap_between_cells)
            column = cell_left // (cell_width + gap_between_cells)
            position = Position(row, column)
            bridges = int(cell.text)
            island = Island(position, bridges)
            islands[position] = island

        max_row = max([position.r for position in islands.keys()])
        max_col = max([position.c for position in islands.keys()])
        matrix = [[islands[position].bridges_count if (position := Position(r, c)) in islands.keys() else 0 for c in range(max_col + 1)] for r in range(max_row + 1)]
        return Grid(matrix)
