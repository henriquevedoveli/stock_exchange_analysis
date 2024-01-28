from tinydb import TinyDB


class DBHandler:
    """
    Classe para lidar com operações de banco de dados.

    Atributos:
    db (TinyDB): Objeto TinyDB representando o banco de dados.
    save_status (bool): Indica o status da última operação de salvamento.
    """

    def __init__(self, db_file="data/database.json") -> None:
        """
        Inicializa o DBHandler.

        Args:
        db_file (str, optional): Caminho para o arquivo do banco de dados. Padrão é "data/database.json".
        """
        self.db = TinyDB(db_file)
        self.save_status = None

    def save_purchase(self, info_stock):
        """
        Salva informações de compra no banco de dados.

        Args:
        info_stock (StockInfo): Objeto contendo informações sobre a compra de ações.
        """
        valores = {key: list(value.values())[0] for key, value in info_stock.to_dict().items()}
        self.db.insert(valores)
        self.save_status = True
