#Revision
#TKINTER Package
#Used fot GUI interface

import tkinter

#Program 1
window1=tkinter.Tk() 
window1.title("Python Course")
# Create content inside the window
#Use either pack() or grid() throughout

label1 = tkinter.Label(window1,text="I Love Python") 
label1.pack()   
# label1.grid(column=0,row=5)                    

label2=tkinter.Label(window1,text="Second Label - Text content 2")
label2.pack()
# label2.grid(column=0,row=2)

window1.mainloop()

#Program 2
#Create Window
window2=tkinter.Tk()
window2.title("Traffic Signal")

label3=tkinter.Label(window2, text="STOP",fg="white",bg="red", padx=52, pady=20)
# label3.grid(row=5, column=2)
label3.pack()

label4=tkinter.Label(window2, text="GO",fg="white",bg="green", padx=57, pady=20)
# label3.grid(row=5, column=2)
label4.pack()

label5=tkinter.Label(window2, text="CAUTION",fg="white",bg="yellow", padx=40, pady=20)
# label3.grid(row=5, column=2)
label5.pack()

# Button Widget
# We can create button widget same as label widget. Perform actions using command parameter
# Perform 
def greet():
    label5=tkinter.Label(window2,text="Welcome")
    label5.pack()

button1=tkinter.Button(window2, text="Greet",command=greet) #Doen not need to call the function. Exvlude ()
button1.pack()

window2.mainloop()

# Entry Widget : Input the data

# Create new window3 and give title to it
window3=tkinter.Tk()        #Top level Widget
window3.title="Entry Widget"

# Create Entry widget and place it
entry1=tkinter.Entry(window3)
entry1.pack()

entry2=tkinter.Entry(window3,bg="yellow",width=50,borderwidth=10)
entry2.pack()

# Add text to entry widget
entry1.insert(0,"Enter your text here ")    #0 : Position of text inside widget

window3.mainloop()