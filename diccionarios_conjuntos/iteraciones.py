products = {
    'laptop': 990,
    'smartphone': 600,
    'tablet': 250,
    'headphones': 70
}

for product, price in products.items():
    print(product, "=>", price)


for index, product in enumerate(products.items()):
    print(index, product)
