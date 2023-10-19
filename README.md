# Análise de Oportunidades na Bolsa de Valores

Este projeto está dividido em duas partes:

## Parte 1: Análise de Oportunidades de Compra de Ações

Nesta parte, realizamos a filtragem de possíveis oportunidades de compra de ações da B3 (Bolsa de Valores do Brasil).

### Fonte de Dados

Os dados podem ser obtidos de três maneiras:

1. **Scrapping da página `fundamentus.com.br/resultado.php`**
2. **Requisição na API `https://brapi.dev/api/quote/list`**
3. **Utilizando um arquivo `data.csv`**

Para este projeto, estamos utilizando a primeira maneira, pois a página da fundamentus fornece mais informações.

### Processamento de Dados

Os dados são tratados e filtrados utilizando as bibliotecas pandas e numpy.

### Interface Gráfica

A interface gráfica é construída utilizando tkinter.

## Parte 2: Análise de Oportunidades de Venda de Ações (Trabalho em Andamento)

Nesta parte, realizamos a filtragem de possíveis oportunidades de venda para ações que foram compradas.

### Fonte de Dados

Pretendemos utilizar o banco de dados TinyDB para guardar as informações de compra.

### Interface Gráfica

Pretendemos utilizar tkinter para construir outra aba de venda.

## Métricas de Análise e Tabela de Interpretação

| Métrica      | Significado Alto            | Significado Baixo          | Sinal para Compra              | Sinal para Venda                |
|--------------|-----------------------------|-----------------------------|-------------------------------|---------------------------------|
| P/L          | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| P/VP         | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| PSR          | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| DY           | Alto retorno em dividendos  | Baixo retorno em dividendos |                               |                                 |
| P/Ativo      | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| P/Cap.Giro   | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| P/EBIT       | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| P/ACL        | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| EV/EBIT      | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| EV/EBITDA    | Sobrevalorizada             | Subvalorizada              | Baixo (Oportunidade de compra) | Alto (Possível venda)          |
| Margem EBIT  | Eficiência operacional alta  | Eficiência operacional baixa | Alta (Oportunidade de compra) | Baixa (Possível venda)         |
| Margem Líquida | Boa eficiência em lucro líquido | Menor eficiência em lucro líquido |                           |                                 |
| Liquidez Corrente | Boa capacidade de cobrir obrigações de curto prazo | Menor capacidade de cobrir obrigações de curto prazo |
| ROIC  | Boa taxa de retorno sobre capital investido | Menor taxa de retorno sobre capital investido | Alto (Oportunidade de compra) | Baixo (Possível venda)         |
| ROE   | Boa taxa de retorno sobre patrimônio líquido | Menor taxa de retorno sobre patrimônio líquido |                          |                                 |
| Pat.Liq.  | Alta liquidez em 2 meses  | Baixa liquidez em 2 meses   |                           |                                 |
| Div.Brut/Pat. | Maior alavancagem financeira | Menor alavancagem financeira |                           |                                 |
| Cresc.5anos  | Alto crescimento em 5 anos | Baixo crescimento em 5 anos |                           |                                 |
