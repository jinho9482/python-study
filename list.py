names = ['Jinho', "Jisung", "Kibo", "Hong"]
names[0] = "Jo"
print(names[:])

nums = [1,2,10,1000,3,0,4,5,7,-1]
max = nums[0]
for num in nums[1:]:
    if num > max:
        max = num
print(max)