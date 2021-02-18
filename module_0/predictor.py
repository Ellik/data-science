import numpy as np

'''
Функция реализована с помощью алгоритма бинарного поиска
'''


def calculate(collection, item):
    # Определяем границы поиска
    left = 0
    right = len(collection) - 1
    attempts = 0
    # Пока существует интервал
    while left <= right:
        attempts += 1
        # Проверка середины
        mid = (left + right) // 2
        predict = collection[mid]
        # Искомый элемент найден
        if predict == item:
            return attempts
        # Много
        if predict > item:
            right = mid - 1
        # Мало
        else:
            left = mid + 1
    # Item не существует в списке
    return None


'''
В функциональном стиле передаем "вычисляющую" функцию в параметре
'''


def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    collection = list(range(1, 101))
    for number in random_array:
        count_ls.append(game_core(collection, number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(calculate)
