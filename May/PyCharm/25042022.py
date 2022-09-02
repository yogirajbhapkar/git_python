#FOR LOOP
#Printing table of 8

print("Table of 8")
for i in range(1,11):       #Note : range is from 1 to 11
    print(8*i)

# Using IF flow control statement for conditional output 
# checking if the citizen is eligible to vote : age 18+ , Take name and age as input

name=input("Enter name of citizen : ")
age=int(input("Enter age : "))

if age>=18:
    print("Mr./Mrs.",name," is eligible for voting")
else:
    print("Your age is less than 18. You're not eligible for voting")

#H/W
#Take score of two players as input , compare the scores and print the winner using IF... ELSE statement 
player1_score=int(input("Enter score of player 1: "))
player2_score=int(input("Enter score of player 2: "))

if player1_score>player2_score:
    print("Player 1 is winner")
if player2_score>player1_score:
    print("Player 2 is winner")