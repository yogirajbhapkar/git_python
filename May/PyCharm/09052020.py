#Positional Arguments : Position of argument is important
def sub(a,b):
    return a-b

ans1=sub(9,6)   #Order is important. here a=9 and b=6
print(ans1)     

#Keyword arguments : We assign a value to varibale in while passing arguments
def sub(a,b):
    return a-b

ans1=sub(b=9,a=6)   #parameters are asigned with respective values
print(ans1)    


#When number of arguments > no of parameters
def add2(p1,p2,*args):
    print("p1 is {}, p2 is {} and remained arguments are {}".format(p1,p2,args))

add2(12,5,11,22,33)
#Note :Here args will be tuple
