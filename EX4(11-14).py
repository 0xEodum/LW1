from auxiliary import *

VOWELS_RU = "аеёиоуыэюя"
VOWELS_EN = "aeiouy"
def count_diff_consonants_vowels(text, language="ru"):
    text = text.lower()

    if language == "ru":
        vowels = VOWELS_RU
    elif language == "en":
        vowels = VOWELS_EN

    vowels_count = sum(1 for letter in text if letter in vowels)
    consonants_count = sum(1 for letter in text if letter.isalpha() and letter not in vowels)

    return consonants_count - vowels_count


def detect_language(strings):
    ru_letters = 0
    en_letters = 0

    for string in strings:
        ru_exists = any(letter in VOWELS_RU for letter in string.lower())
        en_exists = any(letter in VOWELS_EN for letter in string.lower())

        if ru_exists:
            ru_letters += 1
        if en_exists:
            en_letters += 1

        if ru_letters > 0 and en_letters > 0:
            print(f"{colors[2]}[!] Использованы различные языки{Style.RESET_ALL}")
            sys.exit()

    if ru_letters > 0:
        return "ru"
    elif en_letters > 0:
        return "en"


def get_average_ascii(text):
    return sum(ord(c) for c in text) / len(text)

def sort_by_ascii_deviation(strings):
    if check_data_available(strings) == False:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    else:
        reference = get_average_ascii(strings[0])
        def key(text):
            average = get_average_ascii(text)
            deviation = average - reference
            return deviation ** 2

        list_printer(sorted(strings, key=key))


def check_data_available(data):
    if data:
        return True
    else:
        return False

def sort_by_vowels(data):
    lang = detect_language(data)
    if check_data_available(data) == False:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    else:
        sorted_strings = sorted(data, key=lambda x: count_diff_consonants_vowels(x, lang), reverse=False)
        list_printer(sorted_strings)


options = {
        1: sort_by_vowels,
        2: sort_by_ascii_deviation,

    }

if __name__ == '__main__':
    print(f"{colors[3]}$ Выберите задачу: {Style.RESET_ALL}")
    print(f"{colors[0]}1. Сортировка строки в порядке увеличения разницы между количеством согласных и количеством гласных букв в строке.{Style.RESET_ALL}")
    print(f"{colors[1]}2. Сортировка строки в порядке увеличения квадратичного отклонения среднего веса ASCII-кода {'\n'} символа строки от среднего веса ASCII-кода символа первой строки.{Style.RESET_ALL}")
    choice = int(input("Выберите функцию (1-4): "))
    func = options.get(choice)
    if func:
        data = get_strings()
        func(data)

