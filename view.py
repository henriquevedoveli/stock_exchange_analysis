import tkinter as tk
from tkinter import Label, Entry, ttk
from tkinter import messagebox
from metrics import *

#TODO Mostrar o dataframe com os filtros
# TODO Refatorar

class View:
    def __init__(self, df) -> None:
        self.df = df

    def create_metrics_tab(self, frame_metrics, valores_desejados, entry_values):
        for index, valor in enumerate(valores_desejados):
            label = Label(frame_metrics, text=valor, bg="#f0f0f0")
            label.grid(row=index, column=0, sticky="w", padx=(10, 5), pady=5)

            entry = Entry(frame_metrics)
            entry.grid(row=index, column=1, sticky="w", padx=(0, 10), pady=5)
            entry_values.append(entry)

    def create_explanation_tab(self, frame_explanation):
        explanation_text = """
        Digite os valores desejados para cada métrica.
        Os valores serão utilizados para análise de ações.
        """

        explanation_label = Label(frame_explanation, text=explanation_text, bg="#f0f0f0", font=("Arial", 12, "italic"))
        explanation_label.pack(pady=(10, 5), padx=10)

    def create_buttons(self, root, valores_desejados, entry_values):
        show_table_button = tk.Button(root, text="Show DataFrame", command=self.display_dataframe, bg="#4CAF50", fg="white", padx=10, pady=5)
        show_table_button.pack(pady=(0, 10))

        exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#FF5733", fg="white", padx=10, pady=5)

        exit_button.pack(pady=(0, 10))

    def display_filtered_dataframe(self, filters, df):
        try:
            filtered_df = self.apply_filters_to_dataframe(df, filters)

            if filtered_df.empty:
                messagebox.showinfo("Info", "Nenhum valor para exibir após a aplicação dos filtros.")
            else:
                # Exibe o DataFrame filtrado em uma nova janela
                self.display_dataframe(filtered_df)
        except KeyError as e:
            messagebox.showerror("Erro", f"Métrica não encontrada: {str(e)}")



    def apply_filters_to_dataframe(self, df, filters):
        """
        Aplica filtros ao DataFrame.

        Parameters:
        df (pd.DataFrame): DataFrame original.
        filters (list): Lista de filtros no formato [(métrica, valor), ...].

        Returns:
        pd.DataFrame: DataFrame filtrado.
        """
        filtered_df = df.copy()

        for metric, value in filters:
            try:
                value = float(value)  # Converte valor para float
                filtered_df = filtered_df[filtered_df[metric] >= value]
            except ValueError:
                messagebox.showerror("Erro", f"Valor inválido para a métrica '{metric}': {value}")

        return filtered_df
    

    def show_table(self, valores_desejados, entry_values):
        selected_values = []
        for i in range(len(valores_desejados)):
            valor = valores_desejados[i]
            num = entry_values[i].get()
            if num:
                selected_values.append([valor, num])  # Append as a list

        if selected_values:
            self.display_filtered_dataframe(selected_values, df)
        else:
            messagebox.showinfo("Info", "Nenhum valor para exibir.")

    def display_dataframe(self):

        top = tk.Toplevel()
        top.title("DataFrame")
        
        # Crie um Treeview para exibir a tabela
        tree = ttk.Treeview(top)
        tree["columns"] = tuple(self.df.columns)

        # Adiciona os cabeçalhos da tabela
        for col in self.df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)  # Ajuste a largura conforme necessário

        # Adiciona as linhas da tabela
        for _, row in self.df.iterrows():
            tree.insert("", "end", values=tuple(row))

        tree.pack(padx=10, pady=10)