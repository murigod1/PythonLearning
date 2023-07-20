import requests
from bs4 import BeautifulSoup

page = requests.get('https://placaconsultar.com.br/Checkouts/BNJ4I55')
soup = BeautifulSoup(page.content, 'html.parser')

class ParsedItemLocaitor:
    name_concat = 'div.page.animated section.section.section-xs.novi-bg.novi-bg-img.bg-primary.section-transparent div.conteiner div.row.justify-content-center.text-center.row-30 div.col-sm-10.col-lg-8.col-xl-7 h3'

class ParsedItem:

    """"
    A class to take in an HTML page (or part of it). and find properties of an item in it
    """

    def __init__(self):
        self.soup = soup

    @property
    def name_concat(self):
        locaitor = ParsedItemLocaitor.name_concat
        viculoname = self.soup.select_one(locaitor).string
        print(viculoname)

itens = ParsedItem
print(itens.name_concat)