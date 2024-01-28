
from view.buy_tab import BuyTab
from view.metrics_tab import MetricsTab
from tkinter import  ttk
import tkinter as tk

class View:
    def __init__(self, df) -> None:
        self.buy_tab = BuyTab(df)
        self.metrics_tab = MetricsTab(df)
        self.df = df
    
    def create_gui(self) -> None:
        """
        Create a GUI interface to display stock analysis data.

        Args:
            data (DataFrame): The data to display.

        Returns:
            None
        """
        root = tk.Tk()
        root.title("Stock Analysis")
        root.configure(bg="#f0f0f0")

        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, padx=10)

        frame_metrics = ttk.Frame(notebook)
        notebook.add(frame_metrics, text='Métricas')

        valores_desejados = self.df.columns
        entry_values = []

        self.metrics_tab.create_metrics_tab(frame_metrics, valores_desejados, entry_values)

        frame_comprar = ttk.Frame(notebook)
        notebook.add(frame_comprar, text='Comprar')
        self.buy_tab.add_buy_tab_features(frame_comprar)


        root.mainloop()