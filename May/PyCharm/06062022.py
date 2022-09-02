# import tkinter

# # Create window
# window=tkinter.Tk()
# window.geometry("255x372")

# # Create Title
# window.title("Calcuator")

# # Input box : Entry 

# entry1=tkinter.Entry(window,width=39,border=3)
# entry1.grid(row=0,column=0,columnspan=3,padx=10,pady=15)

# #To give functionality to buttons we use lambda function
# #Lambda function is a function with only one expression : One liner

# # Create Buttons and add functionality/Command to it
# # Add command using lambda 

# #When we click on button 1, the command inside it gets executed. here command is execute buttoclick() function with parameter "1"
# #We are using "1" as a string coz it will be useful for us two create multidigit number. Eg. 1+1=2 but "1"+"1"=11
# def buttonclick(num):
#     current=entry1.get()          #Gets the value in entry widget, iitially nothing
#     entry1.delete(0,tkinter.END)  #Once value is stored we clear the entry widget from 0 to end
#     entry1.insert(0,str(current)+str(num))  #Concatenate current value with with num entered


# #When we click button (Say button1) first time

# # Button1 pressed num="1"    button2 pressed num="2"    Button1 pressed num="1"
# # current : nothing          ==> 1                      ==> 12
# # clears the entry widget    ==> clears                 ==> clears the entry widget
# # Inserts : nothing+1==>1    ==> 12                     ==> 121

# def add():
#     firstNumber=entry1.get()
#     global fnum
#     fnum=int(firstNumber)
#     entry1.delete(0,tkinter.END)

# def equal():
#     secondvalue=entry1.get()
#     entry1.delete(0,tkinter.END)
#     entry1.insert(0,fnum+int(secondvalue))

# def clr():
#     entry1.delete(0,tkinter.END)

# button1=tkinter.Button(window,padx=35,pady=20,text="1",command=lambda : buttonclick("1"))

# button2=tkinter.Button(window,padx=35,pady=20,text="2",command=lambda : buttonclick("2"))
# button3=tkinter.Button(window,padx=35,pady=20,text="3",command=lambda : buttonclick("3"))

# button4=tkinter.Button(window,padx=35,pady=20,text="4",command=lambda : buttonclick("4"))
# button5=tkinter.Button(window,padx=35,pady=20,text="5",command=lambda : buttonclick("5"))
# button6=tkinter.Button(window,padx=35,pady=20,text="6",command=lambda : buttonclick("6"))

# button7=tkinter.Button(window,padx=35,pady=20,text="7",command=lambda : buttonclick("7"))
# button8=tkinter.Button(window,padx=35,pady=20,text="8",command=lambda : buttonclick("8"))
# button9=tkinter.Button(window,padx=35,pady=20,text="9",command=lambda : buttonclick("9"))

# button0=tkinter.Button(window,padx=35,pady=20,text="0",command=lambda : buttonclick("0"))

# buttonequal=tkinter.Button(window,padx=76,pady=20,text="=",command=equal)   #No need to call function ()
# buttonplus=tkinter.Button(window,padx=34,pady=20,text="+",command=add)
# buttonclear=tkinter.Button(window,padx=76,pady=20,text="C",command=clr)

# button7.grid(row=1,column=0)
# button8.grid(row=1,column=1)
# button9.grid(row=1,column=2)

# button4.grid(row=2,column=0)
# button5.grid(row=2,column=1)
# button6.grid(row=2,column=2)

# button1.grid(row=3,column=0)
# button2.grid(row=3,column=1)
# button3.grid(row=3,column=2)

# button0.grid(row=4,column=0)
# buttonequal.grid(row=4,column=1,columnspan=2)

# buttonplus.grid(row=5,column=0)
# buttonclear.grid(row=5,column=1,columnspan=2)

# # To give functionality to button we use lambda 
# window.mainloop()

# Program 2 : Perform all four arithmatic operations
#Solution : Add buttons for sub, mult and div and functions for respective opertions
# Add one global variable in operation function

import math
import tkinter

# Create window
window=tkinter.Tk()
window.geometry("255x436")

# Create Title
window.title("Calcuator")

# Input box : Entry 

entry1=tkinter.Entry(window,width=39,border=3)
entry1.grid(row=0,column=0,columnspan=3,padx=10,pady=15)


# Create Buttons and add functionality/Command to it
# Add command using lambda 


def buttonclick(num):
    current=entry1.get()          #Gets the value in entry widget, iitially nothing
    entry1.delete(0,tkinter.END)  #Once value is stored we clear the entry widget from 0 to end
    entry1.insert(0,str(current)+str(num))  #Concatenate current value with with num entered



def add():
    firstNumber=entry1.get()
    global fnum
    global math
    math="addition"
    fnum=int(firstNumber)
    entry1.delete(0,tkinter.END)

def sub():
    firstNumber=entry1.get()
    global fnum
    global math
    math="substraction"
    fnum=int(firstNumber)
    entry1.delete(0,tkinter.END)

def div():
    firstNumber=entry1.get()
    global fnum
    global math
    math="division"
    fnum=int(firstNumber)
    entry1.delete(0,tkinter.END)

def mult():
    firstNumber=entry1.get()
    global fnum
    global math
    math="multiplication"
    fnum=int(firstNumber)
    entry1.delete(0,tkinter.END)

# Write code for each operation in equal function

def equal():
    secondnumber=entry1.get()
    entry1.delete(0,tkinter.END)
    if "addition" in math:
        entry1.insert(0,fnum+int(secondnumber))
    
    if "substraction" in math:
        entry1.insert(0,fnum-int(secondnumber))

    if "division" in math:
        entry1.insert(0,fnum/int(secondnumber))

    if "multiplication" in math:
        entry1.insert(0,fnum*int(secondnumber))


def clr():
    entry1.delete(0,tkinter.END)


button1=tkinter.Button(window,padx=35,pady=20,text="1",command=lambda : buttonclick("1"))

button2=tkinter.Button(window,padx=35,pady=20,text="2",command=lambda : buttonclick("2"))
button3=tkinter.Button(window,padx=35,pady=20,text="3",command=lambda : buttonclick("3"))

button4=tkinter.Button(window,padx=35,pady=20,text="4",command=lambda : buttonclick("4"))
button5=tkinter.Button(window,padx=35,pady=20,text="5",command=lambda : buttonclick("5"))
button6=tkinter.Button(window,padx=35,pady=20,text="6",command=lambda : buttonclick("6"))

button7=tkinter.Button(window,padx=35,pady=20,text="7",command=lambda : buttonclick("7"))
button8=tkinter.Button(window,padx=35,pady=20,text="8",command=lambda : buttonclick("8"))
button9=tkinter.Button(window,padx=35,pady=20,text="9",command=lambda : buttonclick("9"))

button0=tkinter.Button(window,padx=35,pady=20,text="0",command=lambda : buttonclick("0"))

buttonequal=tkinter.Button(window,padx=76,pady=20,text="=",command=equal)   #No need to call function ()
buttonplus=tkinter.Button(window,padx=35,pady=20,text="+",command=add)
buttonclear=tkinter.Button(window,padx=76,pady=20,text="C",command=clr)

buttonsub=tkinter.Button(window,padx=35,pady=20,text="-",command=sub)   #No need to call function ()
buttondiv=tkinter.Button(window,padx=35,pady=20,text="/",command=div)
buttonmult=tkinter.Button(window,padx=35,pady=20,text="*",command=mult)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button0.grid(row=4,column=0)
buttonequal.grid(row=4,column=1,columnspan=2)

buttonplus.grid(row=5,column=0)
buttonclear.grid(row=5,column=1,columnspan=2)

buttonsub.grid(row=6,column=0,columnspan=1)
buttondiv.grid(row=6,column=1,columnspan=1)
buttonmult.grid(row=6,column=2,columnspan=1)


# To give functionality to button we use lambda 
window.mainloop()



