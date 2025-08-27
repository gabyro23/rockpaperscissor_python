options = ["rock", "paper", "scissor"]
winner_user_1 = 0
winner_user_2 = 0

# Pelea
# rock 0 paper 1 paper gana
# rock 0 scissor 2 rock gana
# paper 0 scissor 2 scissor gana

while winner_user_1 < 3 and winner_user_2 < 3:
    user_1 = input("User 1, select rock, paper or scissor: ") 
    user_2 = input("User 2, select rock, paper or scissor: ") 

    if user_1 == user_2:
        print("It's a tie")
    elif user_1 == "rock" and user_2 == "paper":
        print("User 2 won")
        winner_user_2 += 1
    elif user_1 == "scissor" and user_2 == "rock":
        print("User 2 won")
        winner_user_2 += 1
    elif user_1 == "paper" and user_2 == "scissor":
        print("User 2 won")
        winner_user_2 += 1
    else:
        print("User 1 wins")
        winner_user_1 += 1

print(winner_user_1)
print(winner_user_2)

if winner_user_1 > 3:
    print("user 1 is the winner")
else:
    print("user 2 is the winner")
