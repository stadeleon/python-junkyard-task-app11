from Order import Order
from Storage import Storage

storage = Storage()
storage.import_items('articles.csv')

print(storage)
item_id = int(input("Write Article Id to buy: "))
article = storage.get(item_id)
quantity = int(input("Enter the number of items to buy"))

if article.quantity >= quantity:
    order = Order(article, quantity)
    storage.buy_item(article, quantity)
    order.complete()
    storage.export_items('articles1.csv')
print(article)
