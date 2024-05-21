is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price = 1000000
is_good_credit = False
if is_good_credit:
  price *= 0.9
else:
    price *= 0.8
print(f'Down payment: ${price}')

has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan1")

if has_high_income or has_good_credit:
   print("Eligible for loan2")

if has_high_income and ~has_criminal_record:
    print("Eligible for loan3")

print(2 == 2)