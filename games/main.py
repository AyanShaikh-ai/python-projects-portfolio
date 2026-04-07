from art import logo, vs
from game_data import data
import random
print(logo)

def win(f_data, s_data, u_answer):
    answer = ""
    if f_data["follower_count"] > s_data["follower_count"]:
        answer = "A"
    else:
        answer = "B"

    if answer == u_answer:
        return True
    else:
        return False

score = 0
first_entry = random.choice(data)
wrong_answer = False
while not wrong_answer:
    print(f"compare A: {first_entry["name"]}, a {first_entry["description"]}, from {first_entry["country"]}")

    print(vs)

    second_entry = random.choice(data)
    while second_entry == first_entry:
        second_entry = random.choice(data)
    print(f"Against B: {second_entry["name"]}, a {second_entry["description"]}, from {second_entry["country"]}")

    user_choice = input("Who has more followers, type 'A' or 'B': ").upper()

    print("\n" * 30)
    print(logo)

    decision = win(first_entry, second_entry, user_choice)

    if not decision:
        wrong_answer = True
        print(f"Sorry thats wrong, final score: {score} ")
        print(f"{first_entry["name"]} has: {first_entry["follower_count"]} million followers while {second_entry["name"]} has: {second_entry["follower_count"]} million followers")
    elif decision:
        wrong_answer = False
        score += 1
        print(f"Your Right! Current score = {score}")
        print(f"{first_entry["name"]} has: {first_entry["follower_count"]} million followers while {second_entry["name"]} has: {second_entry["follower_count"]} million followers")
        first_entry = second_entry
    else:
        print("error")

