numbers = [5, 2, 5, 2, 2]

for num in numbers:
    print("X" * num)

for x in numbers:
    output = ""
    for y in range(x):
        output += "X"
    print(output)
