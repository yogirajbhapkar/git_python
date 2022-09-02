#Prog - 1
# Write a code to check if a number is a palindrome by taking input from user
word=input("Enter word : ")

if word[::-1]==word:
    print("Given word is Pallidrome")
else: 
    print("Given Word is not Pallidrome")

#Prog - 2
#Same using Function taking given word as parameter

def check_pal(x):
    if x[::-1]==x:
        print("Given Word is palidrome")
    else:
        print("Given word is not pallidrome")

check_pal(word)

#Prob 3
# Write one functio to check pallidrome and other to print result

def check_pall(x):
   return x.casefold==x[::-1].casefold

check_pall(word)

              