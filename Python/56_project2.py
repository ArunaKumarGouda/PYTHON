'''
                    PROJECT 2 - THE PERFECT GUESS
We are going to write a program that generates a random number and ask the user to guees it. 

If the player's guees is higher than the actual number, the program displays "Lower number please". Similarly if the user's guees is too low, the program prints "Higher number please". When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.

Hint: Use the random module.
'''
import random
n = random.randint(1, 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lower number please")
        guesses += 1
    elif(a < n):
        print("Higher number please")
        guesses += 1
print(f"You have guessed the number {n} correctly in {guesses} attempts")
