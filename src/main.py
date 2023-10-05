import tkinter as tk
from tkinter import ttk
from view import *
from scraper import *

# TODO Refatorar
# TODO Tirar qualquer logica daqui

def main():
    global valores_desejados, entry_values

    scrapper = StockScraper()

    view = View(scrapper.data)

    root = tk.Tk()
    root.title("Stock Analysis")
    root.configure(bg="#f0f0f0")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, padx=10)

    frame_metrics = ttk.Frame(notebook)
    notebook.add(frame_metrics, text='Métricas')

    valores_desejados = [
        "Cotacao", "P/VP", "PSR", "DY", "P/Ativo", "P/Cap.Giro", "P/EBIT", "P/ACL", "EV/EBIT", "EV/EBITDA",
        "Mrg.Ebit", "Mrg.Liq.", "Liq.Corr.", "ROIC", "ROE", "Liq.2meses", "Pat.Liq", "Div.Brut/Pat.", "Cresc.5anos"
    ]

    entry_values = []
    view.create_metrics_tab(frame_metrics, valores_desejados, entry_values)

    frame_explanation = ttk.Frame(notebook)
    notebook.add(frame_explanation, text='Explicação')

    view.create_explanation_tab(frame_explanation)
    view.create_buttons(root, valores_desejados, entry_values)

    root.mainloop()

if __name__ == "__main__":
    main()
