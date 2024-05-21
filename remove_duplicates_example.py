# remove duplicated in a list

numbers = [1,2,2,4,4,4,6,2,8,4,23]
new_list = []
for x in numbers:
    if x not in new_list:
        new_list.append(x)
print(new_list)