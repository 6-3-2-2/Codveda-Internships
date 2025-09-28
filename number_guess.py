import random

print('NUMBER GUESSING GAME')
print('------------------------------------------------------------------------------------------------------------')
secret = random.randint(1, 100)
attempts = 7
print(f"You have {attempts} number of guesses.")
for i in range(attempts):
    guess = int(input("Enter guess: "))
    if guess == secret:
        print("🎉 Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Out of attempts! Number was: {secret}")
