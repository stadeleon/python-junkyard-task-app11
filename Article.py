class Article:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.quantity = data['in stock']

    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.quantity}"

