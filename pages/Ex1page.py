from flet import *


class Ex1PAGE(UserControl):
    def __init__(self, page):
        super().__init__()
        self.input = TextField(label="Введите строку")
        self.output = TextField(border_color='black', border_radius=10, border_width=3)
        self.page = page

    def build(self):
        return Column(
            controls=[
                self.input,
                ElevatedButton(text="Посчитать", on_click=self.count_chars),
                self.output,
                ElevatedButton(text="Вернуться в меню", on_click= lambda _: self.page.go('/'))
            ]
        )

    def count_chars(self, e):
        text = self.input.value
        rus_letters = sum(1 for ch in text if ch >= "А" and ch <= "я")
        self.output.value = f"Количество русских букв: {rus_letters}"
        self.update()
