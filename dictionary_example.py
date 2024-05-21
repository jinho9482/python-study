digits = input("Phone: ")
# a,b,c,d = digits
# phone = {a: "One", b: "Two", c: "Three", d: "Four"}
# print(phone[a], phone[b], phone[c], phone[d])

digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for digit in digits:
    output += digit_mapping.get(digit, "!") + " "
print(output)

# 여러가지 선언방법
dict1 = {'sujin': 26, 'bundo': 30, 'jinseuk': 25, 'miram': 25}
dict2 = dict([('banana', 2500), ('apple', 1000), ('mango', 5000)])
dict3 = dict(one = 1, two = 2, three = 3)
print(dict3)