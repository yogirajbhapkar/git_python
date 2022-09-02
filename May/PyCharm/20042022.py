#Tuple
#Creating a tuple
tuple1=(11,22,33,44,33)    #simply put Round Brackets ()
tuple2=tuple((77, "Ram","Sham", True))
tuple3=tuple(["Tomato",34, "Potato", False])

print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

print("Tuple with single element")
#Remember comma , after element if tuple conatins only one element. Else it will take it as string or number 
#With Comma
tuple4=(45,)
tuple5=("String",)
print(type(tuple4))          #O/P : <class 'tuple'>
print(type(tuple5))          #O/P : <class 'tuple'>

#Without Comma
tuple6=(45)
tuple7=("String")
print(type(tuple6))         #O/P : <class 'int'>
print(type(tuple7))         #O/P : <class 'str'>

#Tuple Methods

# .count() Method
print(".count() Method")
a1=tuple1.count(1)
print(a1)

a2=tuple1.count(33)
print(a2)

# .index() Method
print(".index() Method")

a4=tuple1.index(44)  
print(a4)              #O/P : 3

a3=tuple1.index(33)  #Index of 1st appearance of element
print(a3)              #O/P : 2

a5=tuple1.index(33,3,6) #To know the index of element in given range. It gives absolute value i.e4
print(a5)              #O/P : 4

'''a6=tuple1.index(999)    #Gives ValueError if element does not exists
print(a6)'''

#SET

#Eg. Shopping cart : unordered, duplicates not allowed


