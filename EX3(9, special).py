from colorama import Fore, Style

colors = [Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.GREEN]

def sort_by_length(strings, reverse=False):
    return sorted(strings, key=len, reverse=reverse)


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

if __name__ == '__main__':
    str = get_strings()
    print(f"{colors[1]}$ Выберите упорядочивание{Style.RESET_ALL}")
    choose = int(input(f"{colors[1]} (0 - по возрастанию, 1 - по убыванию): {Style.RESET_ALL}"))
    if choose >= 0 and choose <= 1:
        str = sort_by_length(str, choose)
        list_printer(str)
    else:
        print(f"{colors[2]}[!] Введите верный тип упорядочивания{Style.RESET_ALL}")