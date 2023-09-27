import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys 
import pandas as pd
import datetime

acoes = pd.read_csv('acoes-listadas.csv')['Código']

URL = 'http://www.fundamentus.com.br/resultado.php'

HEADERS = {
    'User-Agent'     : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept'         : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT'            : '1',
    'Connection'     : 'close'
}

def fetch_data(url, headers):
    try:
        response = requests.get(url=url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def create_dataframe_from_html(soup):
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
            'PSR': cols[4].text.strip(),
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
    df_filtred = df[df['Papel'].isin(acoes)]
    return df, df_filtred

def save_to_csv(df, filename='data.csv'):
    df.to_csv(filename, index=False)

def convert_to_float(cell):
    try:
        # Remove commas and percentage sign
        cell = cell.replace(',', '').replace('%', '')
        # Substitute comma as decimal separator
        cell = cell.replace('.', '').replace(',', '.')
        # Convert to float
        return float(cell)
    except ValueError:
        return cell


def generate_metrics(df):
    df['Pat.Liq'] = df['Pat.Liq'].str.replace('.', '').str.replace(',', '.').astype(float)
    # df['ROE'] = df['ROE'].str.replace('%', '').str.replace(',', '.').astype(float) / 100
    df['DY'] = df['DY'].str.replace('%', '').str.replace(',', '.').astype(float) / 100

    # Assumindo que cada papel representa uma ação
    df['VPA'] = df['Pat.Liq'] / 1  # Cada papel representa uma ação

    # Convertendo a coluna 'Cotacao' para float
    df['Cotacao'] = df['Cotacao'].astype(float)

    # Calculando o P/VPA (Preço sobre Valor Patrimonial por Ação)
    df['P/VPA'] = df['Cotacao'] / df['VPA']

    # Exibindo o resultado
    print(df[['Papel', 'VPA', 'P/VPA', 'DY', 'ROE']])

def main():
    data = fetch_data(URL, HEADERS)
    soup = BeautifulSoup(data, 'html.parser')
    _, df_filtred = create_dataframe_from_html(soup)

    for column in df_filtred.columns:
        df_filtred.loc[:, column] = df_filtred[column].apply(convert_to_float)

    save_to_csv(df_filtred)

    print(df_filtred)

if __name__ == "__main__":
    main()
