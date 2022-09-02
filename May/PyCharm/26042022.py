#Control Flow Statement : if.. elif.. else Statement
#Erercise 1 : Given geometrical figure is a square or a rectangle

length=float(input("Enter Length : "))
breadth=float(input("Enter Breadth : "))

if length==breadth:
    print("Given Geometric Figure Is Square ")
else: 
    print("Given Geometric Figure Is Rectangle")

#Erercise 2 : Guess the given number
given_num=21
guess=int(input("Enter your guess: "))

if guess<given_num:
    print("You've entered smaller number.")
elif guess>given_num:
        print("You've entered larger number.")
else: 
    print("Your guess is correct")

#Exercise 3 : Give User another chance to enter number one more time in either case

given_num=20
guess=int(input("Enter your guess: "))

if guess<given_num:
    print("You've entered smaller number. Try again")
    guess2s=int(input("Enter your 2nd guess: "))
    if guess2s<given_num:
        print("You've entered smaller number. Better luck next time")
    elif guess2s>given_num :
        print("You've entered larger number. Better luck next time")
    else :
        print("Your guess is correct") 
elif guess>given_num:
    print("You've entered larger number. Try again")
    guess2l=int(input("Enter your 2nd guess: "))
    if guess2l<given_num:
        print("You've entered smaller number. Better luck next time")
    elif guess2l>given_num :
        print("You've entered larger number. Better luck next time")
    else :
        print("Your guess is correct") 
else: 
    print("Your guess is correct")

#Print Formating
#Method 1 : Seperated by comma ,
a=25
print("You have entered number", a)
#Method 2 : f string literals : f"String{variable}"
print(f"You have entered number {a}")
# Method 3 : .format method : "String{}".format({})
print("You have entered number {}".format(a))

#Home Work

#Using conditional operator to compress the code 
ans=6
print("Guess the number batween 1 to 10")
guess1=int(input())

if ans!=guess1:
    if guess1<ans:
        print("Guess Larger Number")
    else : 
        print("Guess smaller number")
    guess1=int(input())
    if guess1==ans:
        print("Your guess is correct")
    else : 
        print("Better luck next time")
else:
    print("Your Guess is correct")