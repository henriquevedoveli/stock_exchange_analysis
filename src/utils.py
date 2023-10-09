import pandas as pd

def convert_to_float(cell):
    try:
        cell = cell.replace(',', '').replace('%', '')
        cell = cell.replace('.', '').replace(',', '.')
        return float(cell)
    except ValueError:
        return cell


class DataLoad:
    def __init__(self, file_path='data/data.csv') -> None:
        self.data = pd.read_csv(file_path)