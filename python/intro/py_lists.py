products = ["Mangoes", "Bananas", "Apples"]

print(products[0])
print(products[-1])

for p in products:
    print(p)

products.append("Kiwi")
print(products)
products.insert(0, "Passion")
print(products)
products.sort(reverse=True)
print(products)

products.remove("Bananas")
print(products)

products.pop(0)
print(products)