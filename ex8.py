# EX8.Create function to sum total of price 
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]

def sum_price(products):
    total = 0
    for products in products:
        total += products["price"]

    return total
print(sum_price(products))