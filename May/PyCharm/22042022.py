dict1={1:"one",2:"Two",4:"Four+",3:"Three",4:"Four",5:"Five",4:"four++++"}
print(dict1)
print(dict1[4]) #Accessing dictionary values using key 

print(dict[6])  #Gives error if key does not exists


#Using get method

a1=dict1.get(2)
print(a1)

a2=dict1.get(6)
print(a2)       #Doesnt give error if key doesn't exists

#Empty Dict
dict2={}
print(type(dict2))

dict3={1}   #This will be set
print(dict3)
print(type(dict3))

#Adding items to Dictionary

dict2[6]="six"
dict2[7]="seven"
print(dict2)

dict1[4]="FOUR"     #Here if we try to add value to existing key, it will take only updated value
print(dict1)        #If we want to add multiple values to same key, we can change the type of value to list
                    # like dict1[4]=["four","four+++","FOUR"] etc

#Add duplicate Key with new value
dict2[7]="seven+"
dict2[7]="seven++"



dict1[4]="FOUR"
print(dict1)
