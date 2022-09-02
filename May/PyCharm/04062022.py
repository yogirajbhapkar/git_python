# Lamda function

def add(a,b):
    c=a+b
    return c

print(add(5,6))



# lamba

sum=lambda c,d : c + d

print(sum(10,12))


odd= lambda x : bool(x%2)

print(odd(15))
print(odd(10))

print(bool(0))
print(bool(1))

import tkinter

# Create window
window=tkinter.Tk()
window.geometry("255x372")

# Create Title
window.title("Calcuator")

# Input box : Entry 

entry1=tkinter.Entry(window,width=39,border=3)
entry1.grid(row=0,column=0,columnspan=3,padx=10,pady=15)


# Create Buttons
# Add command using lambda 
def buttonclick(num):
    current=entry1.get()
    entry1.delete(0,tkinter.END)
    entry1.insert(0,str(current)+str(num))

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




#Entry mail id and password widget


# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# # root window
# root = tk.Tk()
# root.geometry("300x150")
# root.resizable(False, False)
# root.title('Sign In')

# # store email address and password
# email = tk.StringVar()
# password = tk.StringVar()


# def login_clicked():
#     """ callback when the login button clicked
#     """
#     msg = f'You entered email: {email.get()} and password: {password.get()}'
#     showinfo(
#         title='Information',
#         message=msg
#     )


# # Sign in frame
# signin = ttk.Frame(root)
# signin.pack(padx=10, pady=10, fill='x', expand=True)


# # email
# email_label = ttk.Label(signin, text="Email Address:")
# email_label.pack(fill='x', expand=True)

# email_entry = ttk.Entry(signin, textvariable=email)
# email_entry.pack(fill='x', expand=True)
# email_entry.focus()

# # password
# password_label = ttk.Label(signin, text="Password:")
# password_label.pack(fill='x', expand=True)

# password_entry = ttk.Entry(signin, textvariable=password, show="*")
# password_entry.pack(fill='x', expand=True)

# # login button
# login_button = ttk.Button(signin, text="Login", command=login_clicked)
# login_button.pack(fill='x', expand=True, pady=10)


# root.mainloop()