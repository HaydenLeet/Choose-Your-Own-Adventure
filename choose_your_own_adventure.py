# Start
name = input("Type your name: ")
print("Welcome", name, "to this adventure")

# Intro Message
answer = input("Your car ran out of gas in the middle of nowhere on the side of the road, it's the middle of the night and you don't know where you are. Do you stay in your car until the morning or get out and walk to get gas? (Stay/Walk): ").lower()

# Left Option
if answer == "stay":

    # Left Question 1
    answer = input("You hear strange noises coming from the woods next to you. Do you stay in the car or get out to investigate? (Stay/Get Out) ")

    # Left Answer 1 (Correct)
    if answer == "stay":
        print("You stay in your car until the morning. Someone finds you and helps you get gas. You're safe! How boring.")

        # Left Answer 2 (Wrong)
    elif answer == "get out":
        print("You went to investigate the noises and you get greeted by a grizzly bear. You Lose :( ")

        # Invalid Answer (Wrong)
    else:
        print('Not a valid option. You lose.')

# Right Option
elif answer == "walk":
    # Right Question 1
    answer = input("You head out down the road and hear some strange noises. Do you keep going down the road or head into the woods to see what's going on? (Road/Woods) ")

    # Right Answer 1 (Wrong)
    if answer == "woods":
        print("You venture into the woods and hear screaching. You've just stumbled upon a pack of hungry coyotes. You Lose :( ")

    # Right Answer 2 (Correct)
    elif answer == "road":

        # Right Question 2
        answer = input("You follow the road and you see headlights approaching. Do you want to flag the car down and ask for a ride or continue on a solo mission as they might be a killer? (Flag/Solo) ")

        # Right Question 2, Answer 1 (Correct)
        if answer == "solo":
            
            # Right Question 3
            answer = input("You continue walking by yourself and finally you see a small rural town that has one gas station. You get gas and head back to your car several miles back. The locals are a bit suspicious of you and they don't look very friendly. Do you want to ask for a ride back or walk again?: (Ask/Walk)")

            # Right Question 3, Answer 1 (Wrong)
            if answer == "ask":
                print("None of the locals are enjoying your unexpected company. You get too close for their comfort and one of them shoot you in your tracks. You Lose :( ")

            # Right Question 3, Answer 2 (Correct)
            elif answer == "walk":
                print("You continue your journey back the way you came from and eventually make it back to your car with some gas to make it back home. YOU DID IT!")

            else:
                print('Not a valid option. You lose.')

        # Right Question 2, Answer 2 (Wrong)
        elif answer == "flag":
            print("You flag down the car and they stop. You ask for directions or even a ride. The person laughs as he gets out of his car and takes you never to be seen again. You Lose :( ")

        # Invalid Answer (Wrong)
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')

# End Game Message
print("Thank you for trying", name)