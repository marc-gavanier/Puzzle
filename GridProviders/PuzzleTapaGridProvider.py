import math

from bs4 import BeautifulSoup
from playwright.sync_api import BrowserContext

from GridProviders.GridProvider import GridProvider
from GridProviders.PlaywrightGridProvider import PlaywrightGridProvider
from Utils.Grid import Grid


class PuzzleTapaGridProvider(GridProvider, PlaywrightGridProvider):
    def get_grid(self, url: str):
        return self.with_playwright(self.scrap_grid, url)

    def scrap_grid(self, browser: BrowserContext, url):
        page = browser.pages[0]
        page.goto(url)
        html_page = page.content()
        browser.close()
        soup = BeautifulSoup(html_page, 'html.parser')
        cell_divs = soup.select('div.cell, div.tapa-task-cell')
        cells_count = len(cell_divs)
        row_count = int(math.sqrt(cells_count))

        column_count = row_count
        matrix: list[list[bool | list[int]]] = [[False for _ in range(column_count)] for _ in range(row_count)]
        for i, cell_div in enumerate(cell_divs):
            classes = cell_div.get('class', [])
            if 'tapa-task-cell' not in classes:
                continue
            spans = cell_div.select('span')
            values = []
            for span in spans:
                values.append(int(span.get_text()))
            matrix[i // column_count][i % column_count] = values
        return Grid(matrix)
