import random
item_list = [ "rock", "paper", "scissor" ]
user_choice = input("Enter your choice (rock, paper, scissor) : ")
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice}")
print(f"Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both choices are the same. It's a tie!")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Computer wins! Paper covers rock.")
    else:
        print("User wins! Rock crushes scissors.")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Computer wins! Scissors cut paper.")
    else:
        print("User wins! Paper covers rock.")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("User wins! Scissors cut paper.")
    else:
        print("Computer wins! Rock crushes scissors.")



        