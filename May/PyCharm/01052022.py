#Range(start,stop) function
#Start value must be smaller than stop value
range(start,stop,1) : Positive step size
range(stop,start,-1) : Negetive step size

for i in range(0,10):
    print(i)
# for i in range(0,-10):
#     print(i)    #Wont work and wont give error
for i in range(-10,10):
    print(i)
for i in range(20,10,-2):
    print(i) #wont work and wont give error


# -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 Give range(left,right,stepsize) : range(start,stop,2): range(-3,5) 
#O/P : -3 -2- 1 0 1 2 3 4  :Excludes 5, 


# (Start value must be larger than start value)
# range(0,10)
# range(-10,0)
# range(10,0,-1) Reverses the o/p. Start will be stop and stop will be start. 0will be start and 10 will be stop

i=int(input("Enter num : "))
if i in range(21,60,1):
    print("You can drive")
else:
    print("You cant Drive")

for i in range(0,6):
    print(i*"$")

H/W 
for i in range(6,0,-1):
    print(i*"$")

for i in range(7,100,7):
    print(i)
