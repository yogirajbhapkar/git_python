#Dictionary
#DAdding item to dictionary
dict1={1:"one",2:"Two",4:"Four+",3:"Three",4:"Four",5:"Five",4:"four++++"}

#Using update() Method
dict1.update({5:"Five"})
print(dict1)        #{1: 'one', 2: 'Two', 4: 'four++++', 3: 'Three', 5: 'Five'}

#Update existing Item : Using Indexing
dict2= {1: 'one', 2: 'Two', 4: 'four++++', 3: 'Three', 5: 'Five'}
dict2[4]="Four"
print(dict2)        # O/P : {1: 'one', 2: 'Two', 4: 'Four', 3: 'Three', 5: 'Five'}

#Removing Items
#1. Using del Keyword
del dict2[5]
print(dict2)            #O/P : {1: 'one', 2: 'Two', 4: 'Four', 3: 'Three'}

#2. Using pop() Method
dict2.pop(4)
print(dict2)        #O/P : {1: 'one', 2: 'Two', 3: 'Three'}

#If WE again try to remove same item/key or if key is absent, it will give error
#dict2.pop(4)  - It will give error
#dict2.pop(9) - It will give error

#To Avoid error we can set default value in pop() Method
c= dict2.pop(4,"Key Absent")    #This won't give error even if 
print(c)
print(dict2)

#Printing Keys and Values
a=dict2.keys()
print(a)
print(type(a))      #Its type is dict keys - <class 'dict_keys'>

b=dict2.values()
print(b)
print(type(b))      #Its type is dict values - <class 'dict_values'>

#How to INITIALIZE a new dict : using .fromkeys(key,value) Method

dict3=dict.fromkeys(a,"Hi")
print(dict3)        #O/P : {1: 'Hi', 2: 'Hi', 3: 'Hi'}
print(type(dict3))

# COPYING THE COMPLETE DICT TO ANOTHER
dict4=dict1.copy()
print(dict4)    #O/P : {1: 'one', 2: 'Two', 4: 'four++++', 3: 'Three', 5: 'Five'}




