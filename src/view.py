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

        
        filtered_df = self.metrics.apply_filters_to_dataframe(self.df, dicionario)

        for _, row in filtered_df.iterrows():
            tree.insert("", "end", values=tuple(row))

        tree.pack(padx=10, pady=10)
