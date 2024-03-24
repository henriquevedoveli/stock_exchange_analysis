from view.view import View
from data.data_process import ScrapperProcessor
from pandas import DataFrame



def main(gui: bool = False) -> None:
    """
    Main function to process and display stock analysis data.

    Args:
        gui (bool, optional): If True, display a GUI interface. Defaults to False.

    Returns:
        None
    """
    processor = ScrapperProcessor()
    data: DataFrame = processor.build_data_frame("data/data.csv")
    processor.process(data)

    if gui:
        view = View(data)
        view.create_gui()

if __name__ == "__main__":
    main(gui=True)
