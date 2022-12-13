import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
print(logo)



display = []

word_length = len(chosen_word)

for a in range(word_length):
    display += "_"

print(f"{' '.join(display)}")

end = False
lives = 6

while end == False:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
    
        letter = chosen_word[position]

        if letter == guess:
           display[position] = letter
        clear()
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            print("you lost...")
            end = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("congrats you won!")
        end = True
    










