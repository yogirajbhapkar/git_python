#AND, OR Operator
#AND Opeator
#Eg. Driver Recruitment
'''Criteria : Age - Between 18 to 60
Driving Liscence
Education : Graduation Or Exp: 2+ years
Take Name as input'''

nameOfApplicant=input("Please Enter Your Name : ")
ageOfApplicant=int(input("Please Enter Your Age : "))
liscence=input("Do you have driving liscence Yes/No : ")
experience=float(input("Please enter your experience : "))
educationalQual=input("Have you completed your graduation Yes/No : ")

if (60 >= ageOfApplicant >= 18) and (liscence.lower()=="yes") and (experience>=2 or educationalQual.lower()=="yes"):
    print("Mr. {}, You are eligible to apply".format(nameOfApplicant))
else:
    if ageOfApplicant > 60 or ageOfApplicant < 18: #Note
      print(f"You are not eligible to apply as your age={ageOfApplicant}, is not between 18 to 60.")
    elif liscence.lower()=="no":
        print(f"You are not eligible to apply as you don't have driving lincence")
    else:
        print(f"You are not eligible to apply as yor are not fulfilling experience or education criteria")


print("Home Work")

if 0:
    print("True")
else: 
    print("False")

#O/P : False

if 1:
    print("True")
else: 
    print("False")

#O/P : True