from flet import *


class HOME(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                ElevatedButton(text="Задача 1", on_click=lambda _: self.page.go('/Ex1page')),
                ElevatedButton(text="Задача 9", on_click=lambda _: self.page.go('/Ex9page')),
                ElevatedButton(text="Задача 18", on_click=lambda _: self.page.go('/Ex18page'))
            ]
        )
