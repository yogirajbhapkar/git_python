
import tkinter


# Create window
window=tkinter.Tk()
window.geometry("250x340")

# Create Title
window.title("Calcuator")

# Input box : Entry 

entry1=tkinter.Entry(window,width=39,border=3)
entry1.grid(row=0,column=0,columnspan=3)


# Create Buttons

button1=tkinter.Button(window,padx=35,pady=20,text="1")
button2=tkinter.Button(window,padx=35,pady=20,text="2")
button3=tkinter.Button(window,padx=35,pady=20,text="3")

button4=tkinter.Button(window,padx=35,pady=20,text="4")
button5=tkinter.Button(window,padx=35,pady=20,text="5")
button6=tkinter.Button(window,padx=35,pady=20,text="6")

button7=tkinter.Button(window,padx=35,pady=20,text="7")
button8=tkinter.Button(window,padx=35,pady=20,text="8")
button9=tkinter.Button(window,padx=35,pady=20,text="9")

button0=tkinter.Button(window,padx=35,pady=20,text="0")
buttonequal=tkinter.Button(window,padx=76,pady=20,text="=")

buttonplus=tkinter.Button(window,padx=35,pady=20,text="+")
buttonclear=tkinter.Button(window,padx=76,pady=20,text="C")



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

# To give functionality to button we use lambda 
window.mainloop()