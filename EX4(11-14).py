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


if __name__ == '__main__':
    data = get_strings()
    lang = detect_language(data)
    if not data:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    print(f"{colors[1]}$ Выберите упорядочивание{Style.RESET_ALL}")
    choose = int(input(f"{colors[1]} (0 - по возрастанию, 1 - по убыванию): {Style.RESET_ALL}"))
    if choose >= 0 and choose <= 1 and data:
        sorted_strings = sorted(data, key=lambda x: count_diff_consonants_vowels(x, detect_language(data)), reverse=False)
        list_printer(sorted_strings)
    else:
        print(f"{colors[2]}[!] Введите верный тип упорядочивания{Style.RESET_ALL}")
