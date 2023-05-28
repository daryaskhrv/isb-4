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
        logging.info("Данные из файла успешно считаны")
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
        logging.info("Данные успешно записаны в файл")
    except OSError as err:
        logging.warning(f"{err} Не удалось записать данные")


def add_statistics(pools: int, time: float, file_name: str) -> None:
    """
    Функция добавляет данные в файл со статистикой.
    Parameters
    ----------
        pools (int): кол-во процессов
        file_name (str):  путь к файлу
        time (float): время
    Returns
    --------
    """
    try:
        with open(file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([pools, time])
        logging.info("Статистика успешно записана")
    except OSError as err:
        logging.warning(f"{err} Не удалось записать статистику")


def load_statistics(file_name: str) -> dict:
    """
    Функция считывает статистику.
    Parameters
    ----------
        file_name (str):  путь к файлу
    Returns
    --------
        result (dict): считанные данные
    """
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            stats = list(reader)
        logging.info("Статистика успешно считана")
    except OSError as err:
        logging.warning(f"{err} Не удалось считать статистику")
    result = dict()
    for i in stats:
        processes, time = i
        result[int(processes)] = float(time)
    return result