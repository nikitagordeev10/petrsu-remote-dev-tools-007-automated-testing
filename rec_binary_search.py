# Рекурсивный двоичный поиск
def rec_binary_search(target, sequence, first, last):
    """
    Рекурсивный двоичный поиск в отсортированной последовательности.

    :param target: Искомый элемент
    :param sequence: Отсортированная последовательность
    :param first: Начальный индекс поиска
    :param last: Конечный индекс поиска
    :return: True, если элемент найден, иначе False
    """
    # Добавлено в ходе тестирования
    sequence = sorted(sequence)



    if first > last:
        return False
    else:
        mid = (last + first) // 2
        if sequence[mid] == target:
            return True
        elif target < sequence[mid]:
            return rec_binary_search(target, sequence, first, mid-1)
        else:
            return rec_binary_search(target, sequence, mid + 1, last)