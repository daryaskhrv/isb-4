import os
import time
import argparse
import logging
from settings import load_settings
from card_number import enumerate_card_number

SETTINGS_FILE = 'settings.json'
logger = logging.getLogger()
logger.setLevel('INFO')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-set', '--settings', type=str,
                        help='Использовать собственный файл c настройками (Указать путь к файлу)')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-enu', '--enumeration', type=int,
                       help='Поиск номера карты с помощью хеша (указать количество процессов)')
    group.add_argument('-sts', '--statistics',
                       help='Получение статистики, подбор номер карты на разном количестве процессов')
    group.add_argument('-lun', '--lunh_algorithm', help='Проверка валидности номера карты с помощью алгоритма Луна')
    group.add_argument('-vis', '--visualize_statistics', help='Создание гистограмму по имеющейся статистике')
    args = parser.parse_args()
    if args.settings:
        settings = load_settings(args.settings)
    else:
        settings = load_settings(SETTINGS_FILE)
    if settings:
        if args.enumeration:
            card_number = enumerate_card_number(settings,args.enumeration)
            if card_number:
                logging.info(f"Номер карты успешно найден: {card_number}, и записан в файл")
            else:
                logging.info("Не удалось найти номер карты")
