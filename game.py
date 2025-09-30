import random 
words = ["apple","banana","grapes","orange","mango"]
word = random.choice(words)
word_letters = list(word)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []
print("WELCOME TO HUNGMAN GAME")
print("Guess the word, one letter at a time")
print("You have", attempts, "incorrect guessed allowed")
while attempts > 0 and ["_"]:
    print("\nword:", "".join((guessed)))
    print("Used letters:","".join((used_letters)))
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a singal letter")
        continue
    if guess in used_letters:
        print("You have already guessed that letter")
        continue
    used_letters.append(guess)
    if guess in word_letters:
        print("CORRECT GUESS")
        for i, letter in enumerate(word_letters):
            if letter == guess:
                guessed[i] = letter
    else: 
        attempts -= 1 
        print("WRONG GUESS")

if "_" not in guessed: 
    print("CONGRATULATIONS!")
else: 
    print("GAME OVER!")