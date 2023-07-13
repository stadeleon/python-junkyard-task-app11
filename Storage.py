from Article import Article
import pandas as pd
from Order import Order


class Storage:
    def __init__(self):
        self.articles_list = {}

    def add_item(self, article: Article):
        self.articles_list[article.id] = article

    def get(self, item_id: int):
        return self.articles_list[item_id]

    def list(self):
        return self.articles_list

    def buy_item(self, article: Article, quantity: int = 1):
        article.quantity = article.quantity - quantity
        self.articles_list[article.id] = article

    def import_items(self, filename: str):
        df = pd.read_csv(filename, dtype={'id': int, 'price': float, 'in stock': int})
        df = pd.DataFrame(df).to_dict('index')

        for row in df.values():
            self.add_item(Article(row))

    def export_items(self, filename: str):
        with open(filename, 'w') as file:
            file.write(str(self))

    def __str__(self):
        result = 'id,name,price,in stock\n'
        for item in self.articles_list.values():
            result += str(item) + '\n'

        return result
