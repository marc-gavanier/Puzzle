﻿from bs4 import BeautifulSoup
from playwright.sync_api import BrowserContext

from GridProviders.GridProvider import GridProvider
from GridProviders.PlaywrightGridProvider import PlaywrightGridProvider
from Utils.Position import Position
from Utils.Grid import Grid


class PuzzleFutoshikiGridProvider(GridProvider, PlaywrightGridProvider):
    def get_grid(self, url: str):
        return self.with_playwright(self.scrap_grid, url)

    def scrap_grid(self, browser: BrowserContext, url):
        page = browser.new_page()
        page.goto(url)
        html_page = page.content()
        browser.close()
        soup = BeautifulSoup(html_page, 'html.parser')
        cells = soup.find_all('div', class_='cell')
        values = [self.to_value(cell.text) if 'task' in cell['class'] else -1 for cell in cells if 'button' not in cell['class']]
        cells_count = len(values)
        columns_number = sum(1 for cell in cells if 'top: 1px' in cell['style'])
        rows_number = sum(1 for cell in cells if 'left: 1px' in cell['style'])
        if columns_number * rows_number != cells_count:
            raise ValueError("Grid parsing error")
        matrix = []
        for r in range(rows_number):
            row = []
            for c in range(columns_number):
                row.append(values[r * columns_number + c])
            matrix.append(row)
        higher_positions = self.scrap_higher_positions(soup)
        return Grid(matrix), higher_positions

    @staticmethod
    def scrap_higher_positions(soup):
        cell_size = 46
        highers = []
        for div_condition in soup.find_all('div', class_='condition'):
            style = div_condition['style']
            index_row = int(style.split('top: ')[1].split('px')[0]) // cell_size
            index_column = int(style.split('left: ')[1].split('px')[0]) // cell_size
            if any('right' in s for s in div_condition['class']):
                highers.append((Position(index_row, index_column), Position(index_row, index_column + 1)))
            if any('left' in s for s in div_condition['class']):
                highers.append((Position(index_row, index_column + 1), Position(index_row, index_column)))
            if any('up' in s for s in div_condition['class']):
                highers.append((Position(index_row + 1, index_column), Position(index_row, index_column)))
            if any('down' in s for s in div_condition['class']):
                highers.append((Position(index_row, index_column), Position(index_row + 1, index_column)))

        return highers

    @staticmethod
    def to_value(text):
        if text.isdigit():
            return int(text)
        elif text.isalpha() and len(text) == 1:
            return ord(text.upper()) - ord('A') + 10
        else:
            return -1
