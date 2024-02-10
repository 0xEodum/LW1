import re
from colorama import Fore, Style

colors = [Fore.MAGENTA, Fore.CYAN, Fore.BLUE, Fore.RED]
def find_numbers(numbers_row):
    result_list = []
    for i in numbers_row:
        result_list.append(float(i))
    return result_list

def split_to_pairs(input_str):
    result = []
    numbers = re.findall(r'-?\d+(?:\.\d+)*', input_str)
    if numbers:
        for number in numbers:
            num_parts = number.split('.')
            for i in range(len(num_parts)-1):
                pair = f"{num_parts[i]}.{num_parts[i+1]}"
                result.append(pair)
    return result
def find_min_number(data):
    pattern = r'-?\d+(?:\.\d+)*'
    matches = re.findall(pattern, data)
    parsed_values = []
    for i in matches:
        parsed_values += split_to_pairs(i)

    float_numbers_row = find_numbers(parsed_values)
    if not float_numbers_row:
        return None
    else:
        return min(float_numbers_row)

def find_max_number(data):
    pattern = r'-?\d+(?:\.\d+)*'
    matches = re.findall(pattern, data)
    parsed_values = []
    for i in matches:
        parsed_values += split_to_pairs(i)

    float_numbers_row = find_numbers(parsed_values)
    if not float_numbers_row:
        return None
    else:
        return max(float_numbers_row)

def max_consecutive_digits(data):
    max_conc = 0
    cur_conc = 0
    for i in data:
        if i.isdigit():
            cur_conc += 1
        else:
            max_conc = max(max_conc, cur_conc)
            cur_conc = 0
        max_conc = max(max_conc, cur_conc)
    return max_conc


if __name__ == '__main__':
    options = {
        1: find_max_number,
        2: find_min_number,
        3: max_consecutive_digits
    }
    print(f"{colors[3]}$ Выберите задачу: {Style.RESET_ALL}")
    print(f"{colors[0]}1. Найти максимальное из имеющихся в строке вещественных чисел.{Style.RESET_ALL}")
    print(f"{colors[1]}2. Найти минимальное из имеющихся в строке вещественных чисел.{Style.RESET_ALL}")
    print(f"{colors[2]}3. Найти наибольшее количество подряд идущих цифр{Style.RESET_ALL}")
    choice = int(input("Выберите функцию (1-3): "))
    func = options.get(choice)
    if func:
        text = input("Введите текст: ")
        print(func(text))
    else:
        print("Неверный выбор")
