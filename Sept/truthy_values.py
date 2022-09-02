
# TRUTHY VALUES 


# Falsy Values Includes:
# 1) Sequences and Collections:
# Empty lists []
# Empty tuples ()
# Empty dictionaries {}
# Empty sets set()
# Empty strings ” “
# Empty ranges range(0)

# 2) Numbers: Zero of any numeric type.
# Integer: 0
# Float: 0.0
# Complex: 0j

# 3) Constants:
# None
# False



if 1 : #this is always true
    print("I am running")       #OP 
else:
    print("I am  inside else")


if 0 : #this is always false
    print("I am admin")
else:
    print("I am  HR dept")  #OP


# finding boolean values 

print(bool(0))  #False
print(bool(1))  #True
print(bool([])) #False
print(bool({})) #False



if [] : #this is always false since its an empty list
    print("I am admin")
else:
    print("I am  HR dept")  #OP

print("-"*20)

#Home Work

if {} : 
    print("I am inside if")     
else:
    print("I am inside else")   #OP

if {1} : 
    print("I am inside if") #OP
else:
    print("I am inside else")

if {0} : 
    print("I am inside if") #OP
else:
    print("I am inside else")

if [0] : 
    print("I am inside if") #OP
else:
    print("I am inside else")

if -1 : 
    print("I am inside if") #OP
else:
    print("I am inside else")

