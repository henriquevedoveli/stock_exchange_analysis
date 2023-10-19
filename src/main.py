import tkinter as tk
from tkinter import ttk
from view import View
from data.data_process import Scrapper_Processor
from pandas import DataFrame

def create_gui(data: DataFrame) -> None:
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

    valores_desejados = data.columns
    entry_values = []

    view = View(data)
    view.create_metrics_tab(frame_metrics, valores_desejados, entry_values)
    view.create_buttons(root, valores_desejados, entry_values)

    root.mainloop()

def main(gui: bool = False) -> None:
    """
    Main function to process and display stock analysis data.

    Args:
        gui (bool, optional): If True, display a GUI interface. Defaults to False.

    Returns:
        None
    """
    processor = Scrapper_Processor()
    data: DataFrame = processor.build_data_frame()
    processor.process(data)

    if gui:
        create_gui(data)

if __name__ == "__main__":
    main(gui=True)
