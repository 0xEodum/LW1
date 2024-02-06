from flet import *


class Ex18PAGE(UserControl):
    def __init__(self, page):
        super().__init__()
        self.input = TextField(label="Введите строку")
        self.output = TextField(border_color='black', border_radius=10, border_width=3, disabled=True)
        self.page = page
        self.page = page

    def build(self):
        return Column(
            controls=[
                self.input,
                ElevatedButton(text="Найти строку", on_click=self.find_max_digit_row),
                self.output,
                ElevatedButton(text="Вернуться в меню", on_click=lambda _: self.page.go('/'))
            ]
        )
    def find_max_digit_row(self, e):
        data = self.input.value
        maxsubrowlength = 0
        currentsubrowlength = 0
        for i in data:
            if i.isdigit():
                currentsubrowlength += 1
                maxsubrowlength = max(currentsubrowlength, maxsubrowlength)
            else:
                currentsubrowlength = 0
                maxsubrowlength = max(currentsubrowlength, maxsubrowlength)
        self.output.value = maxsubrowlength
        self.update()
