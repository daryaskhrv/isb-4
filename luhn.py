def algorithm_luhn(card_number: str) -> bool:
    """
    Функция проверки корректности номера карты.
    Parameters
    ----------
        card_number (str): номер карты
    Returns
    --------
        True, если номер корректный, иначе False
    """
    card_numbers = list(map(int, card_number))[::-1]
    for i in range(1, len(card_numbers), 2):
        card_numbers[i] *= 2
        if card_numbers[i] > 9:
            card_numbers[i] = card_numbers[i] % 10 + card_numbers[i] // 10
    return sum(card_numbers) % 10 == 0

if __name__ == '__main__':
    print(algorithm_luhn("4466747458361378"))