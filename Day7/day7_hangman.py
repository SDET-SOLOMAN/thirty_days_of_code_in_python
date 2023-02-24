import random
from my_art.hangman_art import stages, word_list, logo

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
game_letters = []

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in game_letters:

        for position in range(word_length):
            if chosen_word[position] == guess:
                game_letters.append(guess)
                display[position] = guess

        if guess not in chosen_word:
            game_letters.append(guess)
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")

    elif guess in game_letters:
        print(guess + f" is already been used {'_'.join(set(game_letters))}")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])