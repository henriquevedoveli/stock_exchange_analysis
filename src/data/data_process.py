import pandas as pd
from data.data_fetcher import Scraper


def convert_to_float(cell):
    """
    Converte uma célula para float.

    Args:
    cell (str): O valor da célula a ser convertido.

    Returns:
    float or str: O valor convertido para float, ou a string original se a conversão falhar.
    """
    try:
        cell = cell.replace(",", "").replace("%", "")
        cell = cell.replace(".", "").replace(",", ".")
        return float(cell) / 100
    except ValueError:
        return cell


class APIProcessor:
    """
    Classe para processar dados de uma API.
    """

    def __init__(self) -> None:
        """
        Inicializa o APIProcessor.
        """
        self.columns = ["stock"]

    def build_data_frame(self, data):
        """
        Constrói um DataFrame a partir dos dados.

        Args:
        data (dict): Dados a serem processados.

        Returns:
        pandas.DataFrame: O DataFrame construído.
        """
        return pd.DataFrame(data["stocks"])


class ScrapperProcessor:
    """
    Classe para processar dados de um web scraper.
    """

    def build_data_frame(self, file_path):
        """
        Constrói um DataFrame a partir de um arquivo CSV ou realiza o scraping se o arquivo não existir.

        Args:
        file_path (str, optional): O caminho para o arquivo CSV. Padrão é "data/data.csv".

        Returns:
        pandas.DataFrame: O DataFrame construído.
        """
        try:
            return pd.read_csv(file_path)
        
        except:
            print("*** Fetching the Data...")
            scrapper = Scraper()
            data = scrapper.data
            return pd.DataFrame(data)

    def process(self, data):
        """
        Processa o DataFrame convertendo as colunas para float.

        Args:
        data (pandas.DataFrame): O DataFrame a ser processado.

        Returns:
        pandas.DataFrame: O DataFrame processado.
        """
        columns_to_convert = data.columns[1:]
        data[columns_to_convert] = data[columns_to_convert].applymap(convert_to_float)
        return data
