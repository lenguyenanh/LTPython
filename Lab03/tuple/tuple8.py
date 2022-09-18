dictionary = {}
tuples = (("akash", 10), ("gaurav", 12), ("anand", 14), 
         ("suraj", 20), ("akhil", 25), ("ashish", 30))
for x,y in tuples:
    dictionary.setdefault(x, []).append(y)
print(dictionary)
from PIL import Image
