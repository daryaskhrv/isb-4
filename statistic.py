import time
import matplotlib.pyplot as plt
from card_number import enumerate_card_number
from work_with_files import add_statistics,load_statistics

def statistic_and_graph(settings: dict)-> None:
    """
    Сбор статистики и создание гистограммы, сохранение ее в файл
    Parameters
    ----------
        settings (dict): параметры
    Returns
    --------
    """
    for i in range(1, 5):
        t1 = time.time()
        enumerate_card_number(settings, i)
        t2 = time.time()
        print(i, (t2 - t1))
        add_statistics(i, t2 - t1, settings['statistics'])
    statistic=load_statistics(settings['statistics'])
    fig = plt.figure(figsize=(18, 9))
    pools = statistic.keys()
    times = statistic.values()
    plt.xlabel('Processes')
    plt.ylabel('Time')
    plt.title('Statistics')
    plt.bar(pools, times, color='gold', width=0.5)
    plt.savefig(settings['png_statistics'])