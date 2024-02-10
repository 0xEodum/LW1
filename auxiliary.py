import sys
import string
from colorama import Fore, Style

colors = [Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.GREEN]
def get_strings():
    strings = []
    while True:
        s = input(f"{colors[0]} Введите строку (оставить пустым для завершения): {Style.RESET_ALL}")
        if not s:
            break
        strings.append(s)

    return strings

def list_printer(data_list):
    for i in data_list:
        print(f"{colors[3]} {i} {Style.RESET_ALL}")