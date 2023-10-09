import tkinter as tk
from tkinter import Label, Entry, ttk
from tkinter import messagebox
from metrics import Metrics

#TODO Mostrar o dataframe com os filtros
# TODO Refatorar

class View:
    def __init__(self, df) -> None:
        self.df = df
        self.metrics = Metrics()


    def create_metrics_tab(self, frame_metrics, valores_desejados, entry_values):
        for index, valor in enumerate(valores_desejados):
            label = Label(frame_metrics, text=valor, bg="#f0f0f0")
            label.grid(row=index, column=0, sticky="w", padx=(10, 5), pady=5)

            entry = Entry(frame_metrics)
            entry.grid(row=index, column=1, sticky="w", padx=(0, 10), pady=5)
            entry_values.append(entry)

    def create_explanation_tab(self, frame_explanation):
        explanation_text = """
    1. P/L (Preço/Lucro):
    - Fórmula: P/L = Preço da ação / Lucro por ação
    - O P/L é a relação entre o preço da ação no mercado e o lucro por ação da empresa. Indica quantas vezes o preço da ação está em relação ao lucro gerado por cada ação.

    2. P/VP (Preço/Valor Patrimonial):
    - Fórmula: P/VP = Preço da ação / Valor patrimonial por ação
    - O P/VP mostra a relação entre o preço da ação no mercado e o valor patrimonial por ação da empresa, indicando se a ação está sendo negociada abaixo ou acima do valor contábil.

    3. PSR (Preço/Sales Ratio):
    - Fórmula: PSR = Preço da ação / Receita líquida por ação
    - O PSR mostra a relação entre o preço da ação e a receita líquida por ação, indicando quantas vezes o preço da ação está em relação à receita gerada.

    4. DY (Dividend Yield):
    - Fórmula: DY = Dividendos por ação / Preço da ação
    - O DY é a taxa de retorno em dividendos que um investidor pode esperar em relação ao preço atual da ação.

    5. P/Ativo (Preço/Ativo):
    - Fórmula: P/Ativo = Preço da ação / Valor total dos ativos por ação
    - O P/Ativo indica quanto o mercado está disposto a pagar em relação ao valor total dos ativos por ação da empresa.

    6. P/Cap.Giro (Preço/Capital de Giro):
    - Fórmula: P/Cap.Giro = Preço da ação / Capital de giro por ação
    - O P/Cap.Giro indica quanto o mercado está disposto a pagar em relação ao capital de giro por ação da empresa.

    7. P/EBIT (Preço/EBIT):
    - Fórmula: P/EBIT = Preço da ação / Lucro antes de juros e impostos (EBIT) por ação
    - O P/EBIT indica quanto o mercado está disposto a pagar em relação ao EBIT por ação.

    8. P/ACL (Preço/Lucro antes de Impostos e Contribuição Social Líquida):
    - Fórmula: P/ACL = Preço da ação / Lucro antes de impostos e contribuição social líquida por ação
    - O P/ACL indica quanto o mercado está disposto a pagar em relação ao lucro antes de impostos e contribuição social líquida por ação.

    9. EV/EBIT (Enterprise Value/EBIT):
    - Fórmula: EV/EBIT = Valor da empresa / Lucro antes de juros e impostos (EBIT)
    - O EV/EBIT é uma métrica que relaciona o valor total da empresa com o lucro antes de juros e impostos, indicando a eficiência operacional da empresa.

    10. EV/EBITDA (Enterprise Value/EBITDA):
        - Fórmula: EV/EBITDA = Valor da empresa / Lucro antes de juros, impostos, depreciação e amortização (EBITDA)
        - O EV/EBITDA é uma métrica semelhante ao EV/EBIT, mas leva em conta a depreciação e a amortização.

    11. Margem EBIT (Mrg.Ebit - Margem Operacional):
        - Fórmula: Mrg.Ebit = (Lucro antes de juros e impostos (EBIT) / Receita total) * 100
        - A Margem EBIT indica a porcentagem da receita total que se converte em lucro operacional antes de juros e impostos.

    12. Margem Líquida (Mrg.Liq.):
        - Fórmula: Mrg.Liq. = (Lucro líquido / Receita total) * 100
        - A Margem Líquida indica a porcentagem da receita total que se converte em lucro líquido.

    13. Liquidez Corrente (Liq.Corr.):
        - Fórmula: Liq.Corr. = Ativos circulantes / Passivos circulantes
        - A Liquidez Corrente indica a capacidade da empresa de cobrir suas obrigações de curto prazo com seus ativos de curto prazo.

    14. ROIC (Return on Invested Capital):
        - Fórmula: ROIC = Lucro líquido / (Patrimônio líquido + Dívida de longo prazo)
        - O ROIC é a taxa de retorno sobre o capital total investido na empresa, incluindo dívidas de longo prazo.

    15. ROE (Return on Equity):
        - Fórmula: ROE = Lucro líquido / Patrimônio líquido
        - O ROE é a taxa de retorno sobre o patrimônio líquido dos acionistas, indicando a eficiência na utilização do capital próprio.

    16. Liquidez em 2 meses (Liq.2meses):
        - Indica a liquidez da ação nos últimos 2 meses, representando a facilidade de comprar ou vender a ação no mercado.

    17. Patrimônio Líquido (Pat.Liq.):
        - Representa o valor contábil da empresa para os acionistas, calculado como Ativos - Passivos.

    18. Dívida Bruta/Patrimônio Líquido (Div.Brut/Pat.):
        - Fórmula: Div.Brut/Pat. = Dívida total / Patrimônio líquido
        - Indica a relação entre a dívida total da empresa e seu patrimônio líquido.

    19. Crescimento em 5 anos (Cresc.5anos):
        - Indica o crescimento percentual acumulado ao longo dos últimos 5 anos em alguma métrica específica (pode variar, por exemplo, lucro, receita, etc.).
    """

        explanation_label = Label(frame_explanation, text=explanation_text, bg="#f0f0f0", font=("Arial", 12, "normal"))
        explanation_label.pack(pady=(10, 5), padx=10)


    def create_buttons(self, root, valores_desejados, entry_values):
        def show_dataframe():
            self.display_dataframe(valores_desejados, entry_values)

        show_table_button = tk.Button(root, text="Show DataFrame", command=show_dataframe, bg="#4CAF50", fg="white", padx=10, pady=5)
        show_table_button.pack(pady=(0, 10))

        exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#FF5733", fg="white", padx=10, pady=5)

        exit_button.pack(pady=(0, 10))


    def display_dataframe(self, valores_desejados, entry_values):
        entry_values_new = []

        top = tk.Toplevel()
        top.title("DataFrame")
        
        tree = ttk.Treeview(top)
        tree["columns"] = tuple(self.df.columns)

        for col in self.df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)  

        for entry in entry_values:
            entry_value = entry.get().replace(',', '.')
            if entry_value:
                try:
                    entry_values_new.append(float(entry_value))
                except ValueError:
                    entry_values_new.append(None)
            else:
                entry_values_new.append(None)

        dicionario = dict(zip(valores_desejados, entry_values_new))

        
        filtered_df = self.metrics.apply_filters_to_dataframe(self.df, dicionario, valores_desejados)

        filtered_df = self.df[
            self.df.apply(
                lambda row: all(
                    row[col] > dicionario[col] if dicionario[col] is not None else True for col in valores_desejados if col in row
                ),
                axis=1
            )
        ]

        for _, row in filtered_df.iterrows():
            tree.insert("", "end", values=tuple(row))

        tree.pack(padx=10, pady=10)
