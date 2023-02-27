from random import randint

# Guess same number as computer, say low if user guess lower or high if higher,
# ask user if they want to play again

keep_playing = True


while keep_playing:

    comp_choice = randint(1, 11)

    user_choice = int(input("Whats your number? "))

    while comp_choice != user_choice:

        if comp_choice < user_choice:
            print('You went too high comrade')
            user_choice = int(input("Whats your number? "))
        else:
            print('You went too low comrade')
            user_choice = int(input("Whats your number? "))

    print(f"Thats right, your pick was {user_choice} and comp pick was {comp_choice}")

    keep_playing = input('Do you want to play again? y/n? ')
    if keep_playing == 'y':
        keep_playing = True
    else:
        print("Good luck")
        keep_playing = False

