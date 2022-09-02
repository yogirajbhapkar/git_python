#TKINTER Package
#Used fot GUI interface

import tkinter

#Anything on window is widget
#Create--.dispaly--position

#To know about waht this Package includes
# print(dir(tkinter))

# help(tkinter) #This will give us documentation link

# Tkinter provides classes which allow the display, positioning and
#     control of widgets. Toplevel widgets are Tk and Toplevel. Other
#     widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,
#     Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox
#     LabelFrame and PanedWindow.

#Basic Syntax same as HTML
# <> Content <>
#window.mainloop() - Last line 

#Program 1
#Create window first --> add title --> Add label with some text --> Align text

# Create window first. This should be the first line
window=tkinter.Tk() 
# Give title to window
window.title("1st GUI Program")

# Create content inside the window
# We create labels in tkinter to create content in window
#syntax : myLabel=tkinter.label(window,text="-------")

label1 = tkinter.Label(window,text="First Label - Text content 1") 

#Display label in window
# There are different methods to place label in window
# myLabel.pack() Method

label1.pack()       #This will palce label1 in window. But its position won't be fixed. It will change with window size

#Align/ Position label 1
#Create one more label, display and psition at dsired location in window

label2=tkinter.Label(window,text="Second Label - Text content 2")

label2.pack()

# label2.grid(column=3,row=0)     #Positioning of label 2 using grid() method

window.mainloop() #This should be last line of Program

