import logging
import csv

logger = logging.getLogger()
logger.setLevel('INFO')

def read_data(file_name: str) -> str:
    """
    Функция считывает данные из txt файла.
    Parameters
    ----------
        file_name (str):  путь к файлу
    Returns
    --------
        data (str): считанные данные
    """
    try:
        with open(file_name, 'r') as f:
            data = f.read()
        logging.info("Данные успешно считаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать данные")
    return data


def write_data(data: str, file_name: str) -> None:
    """
    Функция записывает данные в txt файл.
    Parameters
    ----------
        file_name (str):  путь к файлу
        data (str): данные для записи
    Returns
    --------
    """
    try:
        with open(file_name, 'w') as f:
            f.write(data)
        logging.info("Данные успешно записаны")
    except OSError as err:
        logging.warning(f"{err} Не удалось записать данные")