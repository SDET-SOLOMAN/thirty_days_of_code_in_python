from my_art.insta_game import logo, vs, game_data
from random import choice


def get_random_insta():
    """Gets a random user from our insta database"""
    return choice(game_data)


def format_text_account(account):
    """Returns string to print about insta account"""
    return f"Compare A: {account['name']}, {account['description']}, {account['country']}"


def check_answers(user_guess, insta_a, insta_b):
    """Checks if user guessed it right, returns True or False"""
    if insta_a > insta_b:
        return user_guess == 'a'
    return user_guess == 'b'


def game():
    user_score = 0
    should_we_play = True

    while should_we_play:

        print(logo)

        a = get_random_insta()
        b = get_random_insta()

        while b == a:
            b = get_random_insta()

        if user_score > 0:
            print(f"Yep, your are right, your score is {user_score}")

        print(format_text_account(a))

        print(vs)

        print(format_text_account(b))

        a_follower_count = a["follower_count"]
        b_follower_count = b["follower_count"]
        print(a_follower_count)
        print(b_follower_count)

        user_input = input("Who has more followers A or B: ").lower()

        is_correct = check_answers(user_input, a_follower_count, b_follower_count)

        if is_correct:
            user_score += 1
            print("\n" * 20)
        else:
            print(f"You lost, your score is {user_score}")
            should_we_play = False


game()
