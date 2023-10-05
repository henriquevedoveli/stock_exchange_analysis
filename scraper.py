import requests
import pandas as pd
from bs4 import BeautifulSoup

class StockScraper:
    def __init__(self, url = 'http://www.fundamentus.com.br/resultado.php', path_acoes_listadas='acoes-listadas.csv'):
        self.url = url
        self.data = None

        self.acoes_listada = pd.read_csv(path_acoes_listadas)['Código']

        self.get_data()

    def get_data(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        try:
            response = requests.get(url=self.url, headers=headers, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            self.create_dataframe_from_html(soup, self.acoes_listada)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


    def create_dataframe_from_html(self, soup, acoes):
        table = soup.find('table')
        rows = table.find_all('tr')[1:]

        data_list = []
        for row in rows:
            cols = row.find_all('td')
            data = {
            'Papel': cols[0].text.strip(),
            'Cotacao': cols[1].text.strip(),
            'P/L': cols[2].text.strip(),
            'P/VP': cols[3].text.strip(),
            'PSR': cols[4].text.strip() ,
            'DY': cols[5].text.strip(),
            'P/Ativo': cols[6].text.strip(),
            'P/Cap.Giro': cols[7].text.strip(),
            'P/EBIT': cols[8].text.strip(),
            'P/ACL': cols[9].text.strip(),
            'EV/EBIT': cols[10].text.strip(),
            'EV/EBITDA': cols[11].text.strip(),
            'Mrg.Ebit': cols[12].text.strip(),
            'Mrg.Liq.': cols[13].text.strip(),
            'Liq.Corr.': cols[14].text.strip(),
            'ROIC': cols[15].text.strip(),
            'ROE': cols[16].text.strip(),
            'Liq.2meses': cols[17].text.strip(),
            'Pat.Liq': cols[18].text.strip(),
            'Div.Brut/Pat.': cols[19].text.strip(),
            'Cresc.5anos': cols[20].text.strip()
            }
            data_list.append(data)

        df = pd.DataFrame(data_list)
        self.data = df[df['Papel'].isin(acoes)]