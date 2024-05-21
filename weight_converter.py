weight = int(input("Weight: "))
type = input("(L)bs or (K)g: ")

if type.upper() == "L":
    converted = weight * 0.45
    print(f'{converted}kgs')
    print(converted + 'kgs')
elif type.upper() == "K":
    converted = weight / 0.45
    print(f'{converted}pounds')