Este projeto esta divido em duas partes:

1. Análise de oportunidades de compras de ações:
    Realizar a filtragem de possíveis oportunidades de compras para ações da B3.

    a. Os dados podem ser obtidos de três maneiras:
        * Scrapping da página `fundamentus.com.br/resultado.php`
        * Requisição na API `https://brapi.dev/api/quote/list` 
        * Utilizando um arquivo `data.csv`

        Para este projeto estou utilizando a primeira maneira, já que a página da fundamentus tem mais informações.

    b. Os dados são tratados e filtrados utilizando `pandas` e `numpy`.

    c. A interface gráfica é construida utilizando `tkinter`.

2. Análise de oportunidades de venda de ações (Working In Progress):
    Realizar a filtragem de possíveis oportunidades de vendas para ações que foram compradas.

    a. Pretendo utilizar o banco de dados `TinyDB` para guardar as informações de compra.
    b. Pretendo utilizar o `tkinter` para construir outra aba de venda.

---

1. **P/L (Preço/Lucro)**:
   - **Fórmula**: P/L = Preço da ação / Lucro por ação
   - O P/L é a relação entre o preço da ação no mercado e o lucro por ação da empresa. Indica quantas vezes o preço da ação está em relação ao lucro gerado por cada ação.

2. **P/VP (Preço/Valor Patrimonial)**:
   - **Fórmula**: P/VP = Preço da ação / Valor patrimonial por ação
   - O P/VP mostra a relação entre o preço da ação no mercado e o valor patrimonial por ação da empresa, indicando se a ação está sendo negociada abaixo ou acima do valor contábil.

3. **PSR (Preço/Sales Ratio)**:
   - **Fórmula**: PSR = Preço da ação / Receita líquida por ação
   - O PSR mostra a relação entre o preço da ação e a receita líquida por ação, indicando quantas vezes o preço da ação está em relação à receita gerada.

4. **DY (Dividend Yield)**:
   - **Fórmula**: DY = Dividendos por ação / Preço da ação
   - O DY é a taxa de retorno em dividendos que um investidor pode esperar em relação ao preço atual da ação.

5. **P/Ativo (Preço/Ativo)**:
   - **Fórmula**: P/Ativo = Preço da ação / Valor total dos ativos por ação
   - O P/Ativo indica quanto o mercado está disposto a pagar em relação ao valor total dos ativos por ação da empresa.

6. **P/Cap.Giro (Preço/Capital de Giro)**:
   - **Fórmula**: P/Cap.Giro = Preço da ação / Capital de giro por ação
   - O P/Cap.Giro indica quanto o mercado está disposto a pagar em relação ao capital de giro por ação da empresa.

7. **P/EBIT (Preço/EBIT)**:
   - **Fórmula**: P/EBIT = Preço da ação / Lucro antes de juros e impostos (EBIT) por ação
   - O P/EBIT indica quanto o mercado está disposto a pagar em relação ao EBIT por ação.

8. **P/ACL (Preço/Lucro antes de Impostos e Contribuição Social Líquida)**:
   - **Fórmula**: P/ACL = Preço da ação / Lucro antes de impostos e contribuição social líquida por ação
   - O P/ACL indica quanto o mercado está disposto a pagar em relação ao lucro antes de impostos e contribuição social líquida por ação.

9. **EV/EBIT (Enterprise Value/EBIT)**:
   - **Fórmula**: EV/EBIT = Valor da empresa / Lucro antes de juros e impostos (EBIT)
   - O EV/EBIT é uma métrica que relaciona o valor total da empresa com o lucro antes de juros e impostos, indicando a eficiência operacional da empresa.

10. **EV/EBITDA (Enterprise Value/EBITDA)**:
    - **Fórmula**: EV/EBITDA = Valor da empresa / Lucro antes de juros, impostos, depreciação e amortização (EBITDA)
    - O EV/EBITDA é uma métrica semelhante ao EV/EBIT, mas leva em conta a depreciação e a amortização.

11. **Margem EBIT (Mrg.Ebit - Margem Operacional)**:
    - **Fórmula**: Mrg.Ebit = (Lucro antes de juros e impostos (EBIT) / Receita total) * 100
    - A Margem EBIT indica a porcentagem da receita total que se converte em lucro operacional antes de juros e impostos.

12. **Margem Líquida (Mrg.Liq.)**:
    - **Fórmula**: Mrg.Liq. = (Lucro líquido / Receita total) * 100
    - A Margem Líquida indica a porcentagem da receita total que se converte em lucro líquido.

13. **Liquidez Corrente (Liq.Corr.)**:
    - **Fórmula**: Liq.Corr. = Ativos circulantes / Passivos circulantes
    - A Liquidez Corrente indica a capacidade da empresa de cobrir suas obrigações de curto prazo com seus ativos de curto prazo.

14. **ROIC (Return on Invested Capital)**:
    - **Fórmula**: ROIC = Lucro líquido / (Patrimônio líquido + Dívida de longo prazo)
    - O ROIC é a taxa de retorno sobre o capital total investido na empresa, incluindo dívidas de longo prazo.

15. **ROE (Return on Equity)**:
    - **Fórmula**: ROE = Lucro líquido / Patrimônio líquido
    - O ROE é a taxa de retorno sobre o patrimônio líquido dos acionistas, indicando a eficiência na utilização do capital próprio.

16. **Liquidez em 2 meses (Liq.2meses)**:
    - Indica a liquidez da ação nos últimos 2 meses, representando a facilidade de comprar ou vender a ação no mercado.

17. **Patrimônio Líquido (Pat.Liq.)**:
    - Representa o valor contábil da empresa para os acionistas, calculado como Ativos - Passivos.

18. **Dívida Bruta/Patrimônio Líquido (Div.Brut/Pat.)**:
    - **Fórmula**: Div.Brut/Pat. = Dívida total / Patrimônio líquido
    - Indica a relação entre a dívida total da empresa e seu patrimônio líquido.

19. **Crescimento em 5 anos (Cresc.5anos)**:
    - Indica o crescimento percentual acumulado ao longo dos últimos 5 anos em alguma métrica específica (pode variar, por exemplo, lucro, receita, etc.).


|Métrica                   | Significado Alto                  | Significado Baixo                 | Sinal para Compra                | Sinal para Venda                 |
|--------------------------|----------------------------------|------------------------------------|----------------------------------|---------------------------------|
|**P/L**                    | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**P/VP**                   | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**PSR**                    | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**DY**                     | Alto retorno em dividendos      | Baixo retorno em dividendos       |                                 |                                 |
|**P/Ativo**                | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**P/Cap.Giro**             | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**P/EBIT**                 | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**P/ACL**                  | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**EV/EBIT**                | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**EV/EBITDA**              | Sobrevalorizada                 | Subvalorizada                     | Baixo (Oportunidade de compra)   | Alto (Possível venda)          |
|**Margem EBIT**            | Eficiência operacional alta     | Eficiência operacional baixa     | Alta (Oportunidade de compra)    | Baixa (Possível venda)         |
|**Margem Líquida**         | Boa eficiência em lucro líquido  | Menor eficiência em lucro líquido |                                 |                                 |
|**Liquidez Corrente**      | Boa capacidade de cobrir obrigações de curto prazo | Menor capacidade de cobrir obrigações de curto prazo |  | |
|**ROIC**                   | Boa taxa de retorno sobre capital investido | Menor taxa de retorno sobre capital investido | Alto (Oportunidade de compra) | Baixo (Possível venda) |
|**ROE**                    | Boa taxa de retorno sobre patrimônio líquido | Menor taxa de retorno sobre patrimônio líquido | | |
|**Pat.Liq.**               | Alta liquidez em 2 meses         | Baixa liquidez em 2 meses         | | |
|**Div.Brut/Pat.**          | Maior alavancagem financeira      | Menor alavancagem financeira      | | |
|**Cresc.5anos**           | Alto crescimento em 5 anos       | Baixo crescimento em 5 anos       | | |
