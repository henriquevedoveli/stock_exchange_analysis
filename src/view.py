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
            entry_value = entry.get() 
            entry_values_new.append(entry_value)

        dicionario = dict(zip(valores_desejados, entry_values_new))

        campos_com_valores = [campo for campo, valor in dicionario.items() if valor]

        filtered_df = self.df[self.df[campos_com_valores].astype(float).apply(lambda x: x > float(dicionario[x.name].replace(',', '.')))]

        for _, row in filtered_df.iterrows():
            tree.insert("", "end", values=tuple(row))

        tree.pack(padx=10, pady=10)