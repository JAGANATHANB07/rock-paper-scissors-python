import random

options=("rock", "paper", "scissors")
# player=None
# computer=random.choice(options)
playing=True

while playing:
    player=None
    computer=random.choice(options)
    
    while player not in options:
        player=input("Enter a choice(rock, paper, scissors):  ")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player==computer:
        print("Its's a tie!")
    elif player=="rock" and computer =="scissros":
        print("you are win!")
    elif player=="paper" and computer=="rock":
        print("you are win!")
    elif player=="scissors" and computer=="paper":
        print("you are win!")
    else:
        print("you are lose!")
    
    if not input("You want play again? (y/n): ").lower()=="y":
        playing=False
        
print("Thanks for playing!")





