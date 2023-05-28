import logging
import json

SETTINGS = {
    'hash': '70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473',
    'bin': '446674',
    'last_numbers': '1378',
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