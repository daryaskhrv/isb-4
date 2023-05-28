import logging
import json

SETTINGS = {
    'hash': 'files/hash.txt',
    'bin': 'files/bin.txt',
    'last_numbers': 'files/last_numbers.txt',
    'card_number': 'files/card_number.txt',
    'statistics': 'files/statistics.csv',
    'png_statistics': 'files/statistics.png'
}

def load_settings(settings_file: str) -> dict:
    """
    Считывает из файла параметры.
    Parameters
    ----------
        settings_file (str):  путь до файла c параметрами
    Returns
    --------
        settings (dict): параметры
    """
    settings = None
    try:
        with open(settings_file) as json_file:
            settings = json.load(json_file)
        logging.info('Настройки успешно считаны')
    except OSError as err:
        logging.warning(f'{err} ошибка при чтении из файла {settings_file}')
    return settings


def record_settings(settings_file: str, settings: dict) -> None:
    """
    Записывает в файл параметры.
    Parameters
    ----------
        settings_file (str):  путь до файла с параметрами
        settings (dict): параметры
    """
    try:
        with open(settings_file, 'w') as fp:
            json.dump(settings, fp)
        logging.info('Настройки успешно записаны')
    except OSError as err:
        logging.warning(f'{err} ошибка при записи в файл {settings_file}')


if __name__ == '__main__':
    record_settings('settings.json',SETTINGS)