secret_number = 9
guess_number = 0
guess_limit = 3

while guess_number < guess_limit:
    guess =  int(input("Guess: "))
    guess_number += 1

    if guess == secret_number:
        print("You have won")
        break
else:
    print("Sorry! your failed")