
P=lambda x : print("P",x,"----------------------------------------------")

# filter
# filter is used to filter out the specific data from any iterable
'''syntax x= filter(function, iterable)
    function must return something'''



P(1)
#Filter using loop
ages3=[23,12,56,7,43,9,47,54,34]
 
for x in ages3:
    if x>18:
        print(x)        #Print values above 18+ one by one 

eighteenPlus3=[]
for x in ages3:
    if x>18:
        eighteenPlus3.append(x)
print(eighteenPlus3)        #Print array of values above 18+

P(2)
#Filter using normal function
# filter ages of above above 18 from given list ages=[23,12,56,7,43,9,47,54,34]

ages=[23,12,56,7,43,9,47,54,34]

def ages_above_18(x):
    if x>18:
        return x    #WE can also write - return True
    else:
        return False

eighteenPlus= filter(ages_above_18,ages)
print(eighteenPlus)          #<filter object at 0x0000020C5FA642B0>
print(list(eighteenPlus))    #[23, 56, 43, 47, 54, 34]

for i in eighteenPlus:       #Print values one by one
    print(i)

P(3)
#Filter Using Lambda Function
# filter ages of above above 18 from given list ages1=[23,12,56,7,43,9,47,54,34]

ages1=[23,12,56,7,43,9,47,54,34]

eighteenPlus1= filter((lambda x:x>18),ages1)
print(list(eighteenPlus1))