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
    if not strings:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    else:
        reference = get_average_ascii(strings[0])
        def key(text):
            average = get_average_ascii(text)
            deviation = average - reference
            return deviation ** 2

        list_printer(sorted(strings, key=key))


def sort_by_vowels(strings):
    lang = detect_language(strings)
    if not strings:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    else:
        sorted_strings = sorted(strings, key=lambda x: count_diff_consonants_vowels(x, lang), reverse=False)
        list_printer(sorted_strings)


def get_average_ascii(text):
    return sum(ord(c) for c in text) / len(text)


def get_max_window_average(text, window=3):
    weights = [sum(map(ord, text[i:i+window])) for i in range(len(text)-window+1)]
    return max(w/window for w in weights)

MIN_LENGTH = 3
def sort_by_window_deviation(strings):
    if not strings:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    else:
        for str in strings:
            if len(str) < MIN_LENGTH:
                print(f"{colors[2]}[!] Строка {str} слишком короткая {Style.RESET_ALL}")
                sys.exit()
        def key(text):
            average = get_average_ascii(text)
            window_avg = get_max_window_average(text)
            deviation = average - window_avg
            return deviation ** 2

        list_printer(sorted(strings, key=key))


def sort_by_char_deviation(strings):
    if not strings:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    else:
        freq = max(string.ascii_letters, key=lambda c: sum(w.count(c) for w in strings))
        freq_total = sum(w.count(freq) for w in strings)

        def key(word):
            freq_word = word.count(freq)
            deviation = freq_total - freq_word
            return deviation ** 2

        list_printer(sorted(strings, key=key))

options = {
        1: sort_by_vowels,
        2: sort_by_ascii_deviation,
        3: sort_by_window_deviation,
        4: sort_by_char_deviation
    }

if __name__ == '__main__':
    print(f"{colors[3]}$ Выберите задачу: {Style.RESET_ALL}")
    print(f"{colors[0]}1. Сортировка строки в порядке увеличения разницы между количеством согласных и количеством гласных букв в строке.{Style.RESET_ALL}")
    print(f"{colors[1]}2. Сортировка строки в порядке увеличения квадратичного отклонения среднего веса ASCII-кода {'\n'} символа строки от среднего веса ASCII-кода символа первой строки.{Style.RESET_ALL}")
    print(f"{colors[0]}3. Сортировка строки в порядке увеличения квадратичного отклонения между средним весом ASCII-кода {'\n'} символа в строке и максимального среднего ASCII-кода тройки подряд идущих символов в строке.{Style.RESET_ALL}")
    print(f"{colors[1]}4. Сортировка строки в порядке увеличения квадратичного отклонения частоты встречаемости самого {'\n'} распространенного символа в наборе строк от частоты его встречаемости в данной строке.{Style.RESET_ALL}")
    choice = int(input("Выберите функцию (1-4): "))
    func = options.get(choice)
    if func:
        data = get_strings()
        func(data)

