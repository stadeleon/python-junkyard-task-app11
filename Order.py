from Article import Article
from ReceiptGenerator import ReceiptGenerator


class Order:
    def __init__(self, article: Article, quantity: int):
        self.article = article
        self.quantity = quantity

    def complete(self):
        receipt = ReceiptGenerator()
        receipt.generate(self)
