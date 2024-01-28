import tkinter as tk
from tkinter import ttk, messagebox
from db_handler import DBHandler

class BuyTab:
    def __init__(self, df) -> None:
        self.df = df
        self.database = DBHandler()

    def _create_info_frame(self, frame_comprar, info_stock):
        info_frame = tk.Frame(frame_comprar)
        info_frame.grid(row=2, columnspan=2, padx=10, pady=10)

        for i, (column, value) in enumerate(info_stock.items(), start=1):
            label = ttk.Label(info_frame, text=f"{column}:")
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(info_frame)
            entry.insert(0, info_stock[column].item())
            entry.grid(row=i, column=1, padx=10, pady=5)

        return info_frame

    def _save_purchase(self, info_frame, text_entry, button_submit, info_stock):
        self.database.save_purchase(info_stock=info_stock)
        messagebox.showinfo("Sucesso", "Compra salva com sucesso!")
        info_frame.destroy()
        text_entry.delete(0, tk.END)
        button_submit.grid(row=1, columnspan=2, padx=10, pady=10)

    def _cancel_purchase(self, info_frame, button_submit):
        info_frame.destroy()
        button_submit.grid(row=1, columnspan=2, padx=10, pady=10)

    def _on_button_click(self, text_entry, frame_comprar, button_submit):
        text = text_entry.get().upper()
        info_stock = self.df.loc[self.df['Papel'] == text]
        if not info_stock.empty:
            info_frame = self._create_info_frame(frame_comprar, info_stock)
            button_submit.grid_forget()

            # Configurando uma linha vazia para preencher o espaço abaixo das informações do estoque
            frame_comprar.grid_rowconfigure(len(info_stock)+1, weight=1)

            save_command = lambda: self._save_purchase(info_frame, text_entry, button_submit, info_stock)
            cancel_command = lambda: self._cancel_purchase(info_frame, button_submit)
            save_button = ttk.Button(frame_comprar, text="Salvar Compra", command=save_command)
            save_button.grid(row=len(info_stock)+2, column=0, padx=10, pady=10)
            cancel_button = ttk.Button(frame_comprar, text="Cancelar", command=cancel_command)
            cancel_button.grid(row=len(info_stock)+2, column=1, padx=10, pady=10)
        else:
            messagebox.showinfo("Alerta", "Papel não encontrado!")



    def add_buy_tab_features(self, frame_comprar: tk.Frame) -> None:
        label_text = ttk.Label(frame_comprar, text="Papel:")
        label_text.grid(row=0, column=0, padx=10, pady=10)

        text_entry = ttk.Entry(frame_comprar)
        text_entry.grid(row=0, column=1, padx=10, pady=10)

        button_submit = ttk.Button(frame_comprar, text="Buscar", command=lambda: self._on_button_click(text_entry, frame_comprar, button_submit))
        button_submit.grid(row=1, columnspan=2, padx=10, pady=10)
