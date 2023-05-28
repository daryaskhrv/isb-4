from work_with_files import read_data

def algorithm_luhn(card_number_path: str) -> bool:
    """
    Функция проверки корректности номера карты.
    Parameters
    ----------
        card_number (str): номер карты
    Returns
    --------
        True, если номер корректный, иначе False
    """
    card_number=read_data(card_number_path)
    card_numbers = list(map(int, card_number))[::-1]
    for i in range(1, len(card_numbers), 2):
        card_numbers[i] *= 2
        if card_numbers[i] > 9:
            card_numbers[i] = card_numbers[i] % 10 + card_numbers[i] // 10
    return sum(card_numbers) % 10 == 0