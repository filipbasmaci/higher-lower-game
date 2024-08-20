from random import randint
from art import logo, vs
from game_data import data

print(logo)
print("-----------------------------------------------------""")

is_running = True
score = 0

compare_a_index = randint(0, len(data)-1)
compare_a_follower = data[compare_a_index]["follower_count"]

while is_running:
    compare_b_index = randint(0, len(data) - 1)
    compare_b_follower = data[compare_b_index]["follower_count"]

    print(f"Compare A: {data[compare_a_index]["name"]}, a {data[compare_a_index]["description"]}, from {data[compare_a_index]["country"]}.")
    print(vs)
    print(f"Compare B: {data[compare_b_index]["name"]}, a {data[compare_b_index]["description"]}, from {data[compare_b_index]["country"]}.")

    answer = input("Who has more followers? A or B:").lower()

    if answer == "a" and compare_a_follower >= compare_b_follower:
        score += 1
        compare_a_index = compare_b_index
        compare_a_follower = compare_b_follower
        print("-----------------------------------------------------""")
        print(f"You are right! Current score is: {score}")

    elif answer == "b" and compare_b_follower >= compare_a_follower:
        score += 1
        compare_a_index = compare_b_index
        compare_a_follower = compare_b_follower
        print("-----------------------------------------------------""")
        print(f"You are right! Current score is: {score}")
    else:
        print("-----------------------------------------------------""")
        print(f"Sorry, you are wrong. Final score is: {score}")
        score = 0
        again = input("Do you want to play again? Y/N").lower()
        if again == "y":
            is_running = True
        else:
            is_running = False
            print("Goodbye.")






