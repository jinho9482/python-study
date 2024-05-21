secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    num = int(input("Guess: "))
    guess_count += 1
    if num == 9:
        print("You win!")
        break
else:
    print("You lose!")