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


def get_array():
    input_string = input(f"{colors[0]} Введите строку: \n {Style.RESET_ALL}")
    num_list = input_string.split()

    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def list_printer(data_list):
    for i in data_list:
        print(f"{colors[3]} {i} {Style.RESET_ALL}")

