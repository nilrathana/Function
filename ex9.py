# EX9.Create function to find average of price
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]

def average_price(products):
    average = 0
    for products in products:
      average += products["price"]*10/100


    return average
print(average_price(products))
