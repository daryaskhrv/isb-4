import hashlib
import multiprocessing as mp
from tqdm import tqdm
from typing import Union, Optional

def check_card_number(hash: str, card_number: str) -> Union[str, bool]:
    """
    Функция проверяет, соответствует ли номер карты хешу.
    Parameters
    ----------
        hash (str): хеш
        card_number (str): номер карты
    Returns
    --------
        card_number (str) если хеш совпал, иначе False"""
    true_hash = hashlib.sha256(card_number.encode()).hexdigest()
    if hash == true_hash:
        return card_number
    return False


def enumerate_card_number(hash: str, bins: list, last_numbers: str, pools: int = mp.cpu_count()) -> Optional[str]:
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
    args = []
    for i in range(1000000):
        for bin in bins:
            args.append((hash, f"{bin}{i:06d}{last_numbers}"))
    with mp.Pool(processes=pools) as p:
        for result in p.starmap(check_card_number, tqdm(args, desc="Процесс нахождения номера карты: ",ncols=120)):
            if result:
                p.terminate()
                return result
    return None

if __name__ == '__main__':
    print(enumerate_card_number("70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473",[446674],"1378",3))