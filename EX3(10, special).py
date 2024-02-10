import string
from auxiliary import *
import sys

colors = [Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.GREEN]

def count_words(data):
    return sum([i.strip(string.punctuation).isalpha() for i in data.split()])


if __name__ == '__main__':
    data = get_strings()
    if not data:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    print(f"{colors[1]}$ Выберите упорядочивание{Style.RESET_ALL}")
    choose = int(input(f"{colors[1]} (0 - по возрастанию, 1 - по убыванию): {Style.RESET_ALL}"))
    if choose >= 0 and choose <= 1 and data:
        sorted_strings = sorted(data, key=count_words, reverse=choose)
        list_printer(sorted_strings)
    else:
        print(f"{colors[2]}[!] Введите верный тип упорядочивания{Style.RESET_ALL}")

