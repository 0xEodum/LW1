from colorama import Fore, Style

colors = [Fore.MAGENTA, Fore.CYAN, Fore.BLUE, Fore.RED]

def count_chars(data):
    rus_letters = sum(1 for ch in data if ch >= "А" and ch <= "я")
    return rus_letters

def is_palindrome(data):
    latin_letters = "abcdefghijklmnopqrstuvwxyz"
    filtered_text = ""

    for char in data:
        if char in latin_letters:
            filtered_text += char

    filtered_text = filtered_text.lower()

    return filtered_text == filtered_text[::-1]

def search_date(data):
    dates = []
    days = [str(i).zfill(2) for i in range(1, 32)]
    months = [str(i).zfill(2) for i in range(1, 13)]

    for i in range(len(data)):
        if (data[i:i + 2] in days and
                data[i + 2:i + 3] == '.' and
                data[i + 3:i + 5] in months and
                data[i + 5:i + 6] == '.'):
            date = data[i:i + 10]
            dates.append(date)
    return dates


if __name__ == '__main__':
    options = {
        1: count_chars,
        2: is_palindrome,
        3: search_date
    }
    print(f"{colors[3]}$ Выберите задачу: {Style.RESET_ALL}")
    print(f"{colors[0]}1. Найти общее количество русских символов{Style.RESET_ALL}")
    print(f"{colors[1]}2. Проверить образуют ли строчные символы латиницы палиндром{Style.RESET_ALL}")
    print(f"{colors[2]}3. Найти в тексте даты формата «день.месяц.год»{Style.RESET_ALL}")
    choice = int(input("Выберите функцию (1-3): "))
    func = options.get(choice)
    if func:
        text = input("Введите текст: ")
        print(func(text))
    else:
        print("Неверный выбор")
