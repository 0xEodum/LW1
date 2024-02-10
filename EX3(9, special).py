from auxiliary import *
import sys

colors = [Fore.BLUE, Fore.MAGENTA, Fore.RED, Fore.GREEN]

def sort_by_length(strings, reverse=False):
    return sorted(strings, key=len, reverse=reverse)



if __name__ == '__main__':
    str = get_strings()
    if not str:
        print(f"{colors[2]}[!] Вы не ввели ни единой строки{Style.RESET_ALL}")
        sys.exit()
    print(f"{colors[1]}$ Выберите упорядочивание{Style.RESET_ALL}")
    choose = int(input(f"{colors[1]} (0 - по возрастанию, 1 - по убыванию): {Style.RESET_ALL}"))
    if choose >= 0 and choose <= 1:
        str = sort_by_length(str, choose)
        list_printer(str)
    else:
        print(f"{colors[2]}[!] Введите верный тип упорядочивания{Style.RESET_ALL}")