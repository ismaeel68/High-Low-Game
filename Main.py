# Display art
from art import logo,vs
from game_data  import data
import random

def format_data(account):
    """Takes the account data and returns the  printable formate"""
    account_name=account["name"]
    account_discr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_discr}, form{account_country}"

def check_answer(user_guess,a_followers,b_followers):
    """"Take a user's guess and the follower counts and returns of they got it right."""
    if a_followers > b_followers:
        if user_guess=='a':
            return True
        else:
            return False

print(logo)
score=0
game_should_continue=True
account_b=random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data

    # Making the account at position B become the next account at Position A.
    account_a = account_b
    account_b=random.choice(data)

    if account_a==account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")

    # Ask user for a guess.
    guess=input("Who has more followers? Type 'A' or 'B':").lower()

    # Clear the screen
    print("\n"*20)
    print(logo)

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct= check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score+=1
        print(f"You're right!Current score {score}")
    else:
        print(f"Sorry, that's wrong.Final score{score}")
        game_should_continue=False
