
import pandas as pd

from data.data_fetcher import *

def convert_to_float(cell):
    try:
        cell = cell.replace(',', '').replace('%', '')
        cell = cell.replace('.', '').replace(',', '.')
        return float(cell) / 100
    except ValueError:
        return cell


class API_Processor():
    def __init__(self) -> None:
        self.columns = ['stock']


    def build_data_frame(self, data):

        return pd.DataFrame(data['stocks'])
    

class Scrapper_Processor():
    def __init__(self) -> None:
        pass

    def build_data_frame(self, file_path='data/data.csv') -> None:
        try:    
            return pd.read_csv(file_path)

        except:
            print("*** Fetching the Data...")
            scrapper = Scraper()
            data = scrapper.data

            return pd.DataFrame(data)
        
    def process(self, data):
        columns_to_convert = data.columns[1:]
        data[columns_to_convert] = data[columns_to_convert].map(convert_to_float)


        
        return data
    