list1=[1,2,3,4,5,6,7,8,9]
print(list1)
print(len(list1))

print("-----Accessing the individual element of list -------------------------------------------")

print(list1[4])
print(list1[3:8]) #Excludes 8th element

print("-----Adding items to the list--------------------------------------------------")
print("1. Adding single element (REPLACES)")
list1[4]=14  #5 in list1 will be replaced by 14 and list1 will be updated
print(list1)

print("2. Adding Multiple elements (REPLACES)")
list1[7:9]=[17,18,19,20,21] #Adding Multiple Elements (Replaces)
print(list1)

print("3. Adding elements at the end of list : .append Method")
list1.append(22)
print(list1)

print("4. Adding elements at given index position : .insert Method")
#Shifts other elements to the right
list2=["superman1","superman2","superman3"]
list2.insert(1,"Batman")
print(list2)

print("Joining Two lists : List Concatination")
list3=["Batman1","Batman2","Batman3"]
list4=list2+list3
print(list4)

print("List Methods")
#Sorting
list1.sort()
print(list1)

list1.sort(reverse=True)#For Descending Order
print(list1)

#Making a Copy
l1copy=list1.copy()
print(l1copy)

print("Removing Actual elements of list : .remove Method")
list1.remove(3) #It will remove 3 from list. We can Pass only one argument
print(list1)

#list1.remove(33) Gives error if value doesnt exists

print("Removing element of list : .pop() Method")
list1.pop() #When no index position is given, It will remove last item
print(list1) #1 will be removed

list1.pop(5) #item at index position 5 (17) will be removed
print(list1)

print("Clear : .clear() Method Clears the list")
list1.clear()
print(list1)

print("Home Work")

#Ex.1 Sum of single digit prime numbers from list
primenum=[2,3,5,7]
sum=primenum[0]+primenum[1]+primenum[2]+primenum[3]
print("Sum Of Prime Numbers Below 10 is : ",sum)

#Ex.2 Marks Obtained by students and finding how many scored 100
marks=[87,56,100,56,68,100,90,84,51,67]
c=marks.count(100)
print("100 Marks Obtained by" ,c,"Students")






