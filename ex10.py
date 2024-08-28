# EX10.Show product name that has maximum price


def sum(text):
    name = ""
    max = 0
    for i in range (len(text)):
        if max == 0 :
            max = products[0]["price"]
            name = products[i]["name"]
        if products[i]["price"] > max:
            max = products[i]["price"]
            name = products[i]["name"]

    return name
products = [
    {"name": "Apple", "price": 28},
    {"name": "Orange", "price": 24},
]
print(sum(products))
