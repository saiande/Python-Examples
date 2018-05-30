import math

numbers = list(range(1, 10))
for i in range(2, 10): 
    numbers = list(filter(lambda x: x%2 == 0, numbers))
numbers = list(map(lambda x: math.pow(x, 2), numbers))
print(numbers)