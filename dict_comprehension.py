#{key:value for item in itearble}
#iterable --list or a range
#{1:1,2:4,3:9,4:16,5:25}
# square={}
# for num in range(1,6):
#     square[num]=num**2
# print(square)

# square={num:num**2 for num in range(1,6)}
# print(square)

# product={"apple":1.00,"banana":0.50,"orange":0.25,"milk":1.50}
# print(product)
# disc_product={product:price*0.9 for product,price in product.items()}
# print(disc_product)
# dict2={product:price*0.9 for product,price in product.items() if price>1}
# print(dict2)
# names=['Ammu','Sam',"ninu"]
# dict1={name.lower():name.upper() for name in names}
# print(dict1)
str="coding hives"
my_iter=iter(str)
print(next(my_iter))
print(next(my_iter))