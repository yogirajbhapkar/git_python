# 08042022
P=lambda x : print("P",x,"----------------------------------------------")

# Error and Exception Handling
# help(Exception)


P(1)

# print(b)        #This wil create name error. And program will stop running 

print("Hello")

# T/f We need to handle the error
# We do it using try-except block

P(2)
try:
    print(b)
except:
    print("Some Error occured")

print("Hello")

# In above example error won't appeaer. It will print "Some Error occured"and execute next lines

P(3) 
# There are inbuild exceptions defined in exception class.
# They can be accessed as below

try:
    print(23/0)
except Exception as e :
    print(e)


# Handling the Error
'''Identify the error manually and give user a message
'''
P(4)
try:
    print(23/0)
except ZeroDivisionError:
    print("Give some message to User***")
    print("Division by zero is not possible")

#Handling multiple errors
#Handles first arrived error only????????????????????????????????????????
P(5)
try :
    print(25/a)
    print(12/0)
except NameError as e:
    print("Variable a is not Defined")  #User defined 
    print(e)        #This resposne is from inbuilt class
except ZeroDivisionError:
    print("Can't divide by zero")

