matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# for row in matrix:
#     for item in row:
#         print(item)

numbers = [5, 2, 4, 1, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.insert(-1, 10)
print(numbers)
numbers.insert(100, 10)
print(numbers)
numbers.remove(4)
print(numbers)
# numbers.clear()
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(1))
# print(numbers.index(50))
print(50 in numbers)
print(numbers.count(10))
print(numbers.sort()) # None: absence of value
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers3 = numbers
numbers.append(10)
print(numbers2)
print(numbers3)
