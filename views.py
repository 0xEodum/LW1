from flet import *
from pages.Ex1page import Ex1PAGE
from pages.Ex9page import Ex9PAGE
from pages.Ex18page import Ex18PAGE
from pages.Home import HOME

def views_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          HOME(page)
        ]
      ),
    '/Ex1page':View(
        route='/Ex1page',
        controls=[
          Ex1PAGE(page)
        ]
      ),
      '/Ex9page': View(
          route='/Ex9page',
          controls=[
              Ex9PAGE(page)
          ]
      ),
      '/Ex18page': View(
          route='/Ex18page',
          controls=[
              Ex18PAGE(page)
          ]
      ),
  }