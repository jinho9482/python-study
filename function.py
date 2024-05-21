def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


print("Start")
greet_user("Jinho", "Jo") # positional arguments
greet_user(last_name = "Jane", first_name="Mary") # keyword arguments, for readability
# keyword arguments should come after positional arguments when used at the same time
greet_user( "Jo", last_name = "Jinho")

print("Finish")

# By default, all the functions return "None" object

def square(number):
    return number * number

print(square(2))