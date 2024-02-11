from auxiliary import colors, list_printer, get_array
from colorama import Style, Fore

def right_cyclic_shift(array, shift_value):
    shift = -1 * shift_value
    print(f"{colors[3]} Список после сдвига: {array[shift:] + array[:shift]}")

def num_of_even(array):
    counter = 0
    for i in array:
        if i % 2 == 0:
            counter += 1
    print(f"{colors[3]}Количество чётных: {counter} {Style.RESET_ALL}")


def count_of_minimal(array):
    min_element = min(array)
    k = array.count(min_element)
    print(f"{colors[3]}Количество минимальных элементов ({min_element}) равно: {k} {Style.RESET_ALL}")


def sort_by_count(array):
    count = {}
    for n in array:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    result = []
    while count:
        max_num = max(count, key=count.get)
        max_count = count[max_num]
        result.extend([max_num] * max_count)
        del count[max_num]

    print(f"{colors[3]}Отсортированный список: {result} {Style.RESET_ALL}")


options = {
        1: right_cyclic_shift,
        2: right_cyclic_shift,
        3: num_of_even,
        4: count_of_minimal,
        5: sort_by_count

    }

if __name__ == '__main__':
    print(f"{colors[3]}$ Выберите задачу: {Style.RESET_ALL}")
    print(f"{colors[0]}1. Циклический сдвиг вправо на 2 позиции.{Style.RESET_ALL}")
    print(f"{colors[1]}2. Циклический сдвиг вправо на 1 позицию.{Style.RESET_ALL}")
    print(f"{colors[0]}3. Найти количество чётных элементов.{Style.RESET_ALL}")
    print(f"{colors[1]}4. Найти количество минимальных элементов.{Style.RESET_ALL}")
    print(f"{colors[0]}5. Сортровка в порядке встречаемости эелемента.{Style.RESET_ALL}")
    choice = int(input("Выберите функцию (1-5): "))
    func = options.get(choice)
    if func:
        data = get_array()
        match choice:
            case 1:
                shift_value = 2
                func(data, shift_value)
            case 2:
                shift_value = 1
                func(data, shift_value)
            case 3:
                func(data)
            case 4:
                func(data)
            case 5:
                func(data)