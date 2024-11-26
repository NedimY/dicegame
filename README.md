README.md
Hello my program which is a dice game, is designed as a single player game to roll 3 dice and add up your total score. The game ends when the player decides they're satisfied with the score they have recieved.

First the program implements the library random so that it can help them when it gets to randomly generating a number for the dice.
The code starts with welcoming the player to my game and asking them to press 1 to play.
When the user enters 1 it will start rolling their die. If they press anything other than 1 then the program will show an error and quit on them.
I defined the variable roll which is where I have the 3 differnt dice that will randomly generate a number 1-6 for each.
I also created a variable named difference which will spot the number that's different among the 3 dice. This will help in making the other two numbers fixed and giving the user a chance to only roll the number that's different.
I then accounted for every condition that the dice wil produce and what it will return if the condition is met.
The empty list "Mylist" will store all the numbers that the dice produce and show in the termianl the numbers the user got and add up their total.
If the numbers that the user got are all the same then they recieve zero points and their turn ends and they cannot reroll.
If two of the numbers are the same no matter which dice it is (dice1 and dice2 or dice and dice3) they will be fixed and cannot be rolled but the number that's different can be.
If none of the numbers are the same the user will be prompted to reroll all 3 dice if they choose to which is what the "while" loop is responsible for.
If they decided to keep on rolling the game will only stop if all 3 numbers are the same or if they choose "n" when they're asked to reroll.

