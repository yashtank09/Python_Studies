import random
from datetime import datetime

a = datetime.now().date()
# print(a)

# tomorrow = a.strftime('%d/%m/%Y')
b = a.strftime('%m/%d/%Y')
print (b)