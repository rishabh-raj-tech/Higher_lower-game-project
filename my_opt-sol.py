from Data import data
import random

def player_data(player_data):
    name = player_data["name"]
    description = player_data["description"]
    country = player_data["country"]
    return f"{name}, a {description} from {country}"

def compare(guess, followers_a, followers_b):
    if followers_a >  followers_b:
        return guess == "a"
    elif followers_b > followers_a:
        return guess == "b"

def engine():

    score = 0
    progress = True

    player_a = random.choice(data)
    player_b = random.choice(data)

    while progress:
        player_a = player_b
        player_b = random.choice(data)

        while player_a == player_b:
            player_b = random.choice(data)

        print(f"compare A: {player_data(player_a)}")
        print("v/s")
        print(f"compare B: {player_data(player_b)}")

        user_input = input("choose who has the highest instagram followers: A or B: ").lower()

        follower_a_count = player_a["follower_count"]
        follower_b_count = player_b["follower_count"]

        if_correct = compare(user_input, follower_a_count, follower_b_count)

        print("\n" * 20)

        if if_correct:
            score += 1
            print(f"you are right! your current score: {score}")
        else:
            progress = False
            print(f"sorry, that's wrong, final score: {score}")

engine()