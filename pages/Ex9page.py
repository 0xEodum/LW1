from flet import *
import re


class Ex9PAGE(UserControl):
    def __init__(self, page):
        super().__init__()
        self.input = TextField(label="Введите строку")
        self.output = TextField(border_color='black', border_radius=10, border_width=3, disabled=True)
        self.page = page
    def build(self):
        return Column(
            controls=[
                self.input,
                ElevatedButton(text="Найти дробь", on_click=self.find_min_rational),
                self.output,
                ElevatedButton(text="Вернуться в меню", on_click=lambda _: self.page.go('/'))
            ]
        )

    import re

    def find_min_rational(self, e):
        data = self.input.value

        numbers = []

        # Ищем все числа в строке
        current_num = ""
        dot_met = False

        for char in data:
            if char in "0123456789.-":
                if char == "." and dot_met:
                    # Встретили вторую точку,
                    # значит число закончилось
                    numbers.append(float(current_num))
                    current_num = ""
                    dot_met = False
                else:
                    if char == ".":
                        dot_met = True
                    current_num += char
            elif current_num:
                numbers.append(float(current_num))
                current_num = ""
                dot_met = False

        # Находим минимум
        min_number = numbers[0]
        for num in numbers:
            if num < min_number:
                min_number = num
        self.output.value = f"Минимальное рациональное число: {min_number}"

        self.update()

