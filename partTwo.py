import random
secret_number = random.randint(1, 10)
x = int(input("Guess the number from 1 to 10"))
if x > secret_number:
    print("Too high")
elif x < secret_number:
    print("too low")
elif x := secret_number:
    print("You're correct")
