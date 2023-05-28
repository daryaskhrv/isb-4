import hashlib
import multiprocessing as mp
from tqdm import tqdm
from typing import Union, Optional
from work_with_files import write_data

def check_card_number(hash: str, card_number: str) -> Union[str, bool]:
    """
    Функция проверяет, соответствует ли номер карты хешу.
    Parameters
    ----------
        hash (str): хеш
        card_number (str): номер карты
    Returns
    --------
        card_number (str) если хеш совпал, иначе False
    """
    true_hash = hashlib.sha256(card_number.encode()).hexdigest()
    if hash == true_hash:
        return card_number
    return False


def enumerate_card_number(settings: dict,pools: int = mp.cpu_count()) -> Optional[str]:
    """
    Функция подбирает номер карты.
    Parameters
    ----------
        hash (str): хеш
        bin (list): список бинов
        last_numbers (str): последние 4 цифры карты
        pools (int): кол-во ядер
    Returns
    --------
        result (str): номер карты, если найден
    """
    hash=settings['hash']
    bin=settings['bin']
    last_numbers=settings['last_numbers']
    args = []
    for i in range(1000000):
        args.append((hash, f"{bin}{i:06d}{last_numbers}"))
    with mp.Pool(processes=pools) as p:
        for result in p.starmap(check_card_number, tqdm(args, desc="Процесс нахождения номера карты: ",ncols=110)):
            if result:
                p.terminate()
                write_data(result,settings['card_number'])
                return result
    return None