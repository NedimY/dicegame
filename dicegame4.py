import random

# Asking the user if they want to play a dice game
play_dice = input("Hello, welcome to my dice game! Press 1 to play! ")
if play_dice == "1":
    print("Okay, rolling your dice! ")
else:
    print("An error occurred, goodbye!")
    quit()

# Function to roll three dice
def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    return [dice1, dice2, dice3]



# Roll the dice and calculate results
mylist = roll()
print("First roll:", mylist)
total = sum(mylist)

# Check if all dice are the same
if difference(mylist) == 0:
    print("You have tupled out and have ZERO points!")
else:
    while True:
        print(f"Your first die was a {mylist[0]}, your second die was a {mylist[1]}, your third die was a {mylist[2]}.")
        print(f"Your total is {total}.")
        
    # Determine the different die
        diff_result = difference(mylist)
        # If all dice are the same
        if diff_result == 0:
            #This will give the user zero points if all their dice are the same
            print("All dice are now the same. You have tupled out and have ZERO points!")
            break
        #If All dice are different
        elif diff_result[0] == "different_dice":  
            print("All three dice are different!")
        #Ask the user if they want to reoll all dice or stop playing
            reroll_choice = input("Do you want to reroll all dice or stop? (roll/stop) ")
            if reroll_choice.lower() == "roll":
            #Reroll all dice
                mylist = roll()  
                #Recalculate the total
                total = sum(mylist)  
                #Print the reroll from the list
                print("After reroll:", mylist)
                # Continue the game
                continue  
            #If the user decides to stop playing the game
            else:
                print("You chose to stop. Final dice:", mylist)
                print(f"Your final total is {total}.")
                break
        #If one die is different
        else:  
        #This will print the die that's not the same as the others and ask them to reoll the dice that's different
            print(f"The die with the value of {diff_result[0]} is different from the other two dice!")
            go_again = input("Do you want to reroll the different die? (y/n) ")
            if go_again.lower() == "y":
                #Reroll the different die
                mylist[diff_result[1]] = random.randint(1, 6)
                total = sum(mylist)  
                #Recalculate the total
                print("After reroll:", mylist)
            else:
            #The user doesn't want to reroll this will present their total and stop
                print("No more rerolls. Final dice:", mylist)
                print(f"Your final total is {total}.")
                break
