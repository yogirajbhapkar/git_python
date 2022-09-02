#List Methods

list1=["Mandar",23,"Ram","Sham",45,True]

#.append(x) Method
a1=list1.append("Tomato") #Returns None
print(a1)
print(list1)

#.extend(iterable) Method
list2=["Ram",True,64]
print(list2)
"""
list2.extend(2)  #2 is int and integers are not iterable. It will give error
print(list2)     #Error
"""

list2.extend("2") #Here 2 is string and strings are iterable. Can be extended
print(list2)      #O/P : ['Ram', True, 64, '2']

a21= list2.extend("Pat")       #String extended
print(a21)                     #Returns None
print(list2)                  # See the o/p : ['Ram', True, 64, '2', 'P', 'a', 't']

a22=list2.extend([1,"go",3])    #List Extended
print(list2)                   # O/P :['Ram', True, 64, '2', 'P', 'a', 't', 1, 'go', 3]

list2.extend((33,44,55))    #Tuple Extended
print(list2)                # O/P : ['Ram', True, 64, '2', 'P', 'a', 't', 1, 'go', 3, 33, 44, 55]

#insert(i,x) Method : Inserts element at specified location
list3=[False, "Sham", 3]

a31=list3.insert(0,34)
print(a31)          #Rteturns None
print(list3)        #34 will be added at index position 0. O/P : [34, False, 'Sham', 3]

list3.insert(len(list3),"Ram")  #"Ram" will be added at index position 4 i.e length of list3
print(list3)                    #[34, False, 'Sham', 3, 'Ram']

'''list3.insert(99)    #Error if Index position is not given
print(list3)

list3.insert(2,)    #Error if element is not given
print(list3)'''

list3.insert(2,[11,22,33])   #List inserted
print(list3)                 # O/P :  [34, False, [11, 22, 33], 'Sham', 3, 'Ram']

list3.insert(1,("AA","BB"))   #Tuple inserted
print(list3)                 # O/P :  [34, ('AA', 'BB'), False, [11, 22, 33], 'Sham', 3, 'Ram']

print(".remove(x) Method") # Removes given element 
list4=[34, False, [11, 22, 33], 'Sham', 'Ram']

a41=list4.remove(False) #Remove False from list
print(a41)
print(list4)        # O/P : [34, [11, 22, 33], 'Sham', 'Ram']

#list4.remove(11)     #Gives error if element not present in the list

#-------------------------------------------------------------------------------------------------

print(".pop([i]) Method") # Removes Element at Specified Location
list5= [34, False, [11, 22, 33], 'Sham', 'Ram']
a51=list5.pop(2)    #Returns element at index position 2, here list
print(a51)          #O/P : [11, 22, 33]
print((list5))      #O/P : [34, False, 'Sham', 'Ram']

a52=list5.pop()    #If index position not specified, removes the last element
print(a52)         #O/P :  Ram
print(list5)       #O/P :  [34, False, 'Sham']

'''a53=list5.pop(1:3) #Gives error. We can't give range here
print(list5)'''

#------------------------------------------------------------------------------------------
print('.clear() Method')  #Clears the list
list6=['Sham', True, 44 ,'Ram']

a61=list6.clear()      
print(a61)              #Returns None
print(list6)            #Empty list -- O/P : []
print(type(list6))      #Still list but empty list

#-------------------------------------------------------------------------------------------
print(".index(x) Method")  #Gives Index of first appeared element

list7=['Sham', True, 44 ,'Ram',44,"Bam"]

a71=list7.index(44) #Here There are two 44
print(a71)          #gives index of first appeared 44 -- O/P : 2
print(list7)

#If same item repeats multiple time, give range of indices and limit the search
#list.index(x,start,end)
#The returned index is calculated relative to the beginning of list rather than the start argument

a72=list7.index(44,3,6) #Here index of 2nd appeared 44 will be cacl. relative to begining of list
print(a72)              #O/P : 4

'''a73=list7.index(11)
print(a73)      #ValueError as 11 is not in list7'''

#-------------------------------------------------------------------------------------------------
print(".count(x) Method")  #Counts no of times x appeared in the list

list8=['Sham', True, 44 ,'Ram', True]

a81=list8.count(True)       #Count how many time True is appeared in the list
print(a81)                  # O/P : 2
print(list8)                

a82=list8.count(123)       #Count how many time 123 is appeared in the list
print(a82)                  # O/P : 0

#---------------------------------------------------------------------------------------------------
print(".copy() Method")  #Returns a copy of the list
list9=['Sham', True, 44 ,'Ram']

a91=list9.copy()
print(a91)

#---------------------------------------------------------------------------------------------------
print(".reverse() Method")  #Reverses the order of the list
                            #Changes Original list
list10=['Sham', True, 44 ,'Ram']

a101=list10.reverse()
print(a101)         #Returns None O/P : None
print(list10)       # Reversed list O/P : ['Ram', 44, True, 'Sham']

#-----------------------------------------------------------------------------------------------------
print(".sort() Method")  #Sorts list alphabetically ascending order. same with numbers

# list11=['Sham', True, 44 ,'Ram',"Tom"] #sorting list with mixed elements (int, bool, string) gives error

list11=['Sham','som','Ram','Tom', 'dom'] 
a111=list11.sort()  #Capital letters first then small letters
print(a111)         #Returns None
print(list11)       #Changes Original list O/P : ['Ram', 'Sham', 'Tom']

list11a=[11,54,786,-10,1.2]   
list11a.sort()      # -ve --> 0 --> +ve
print(list11a)      # Changes Original list O/P : [-10, 1.2, 11, 54, 786]

list11b=['som','Ram','Tom', 'dom'] 
list11b.sort(reverse=True)   #Reverse=True for Descending Order
print(list11b)








