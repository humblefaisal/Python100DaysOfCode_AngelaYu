# def add(*num):
#     sum=0
#     for n in num:
#         sum+=n
#     return sum

# print(add(1,2,3,4,5,6))

# ok
# def calculate(n,**kw):
#     n+=kw["add"]
#     n*=kw["multiply"]
#     return n

# print(calculate(5,add=1,multiply=2))


# error 

# def calculate(n,**kw):
#     n+=kw["add"]
#     n*=kw["multiply"]
#     return n

# print(calculate(5,add=1))

# import tkinter as tk

# def button_action():
#     window.after(2000,lambda :bttn.config(text="Button"))
#     window.after(2000,lambda :my_label.config(text="My Label"))
#     bttn.config(text="Ouch!")
#     my_label.config(text=entry.get())

# window = tk.Tk()
# # window.config(title="My Window")
# window.minsize(width=500,height=500)
# window.title("My Window")
# my_label = tk.Label(text="my Label")
# my_label.config(text="mytext")
# my_label.pack()
# # my_label["text"] = "My Text"
# bttn = tk.Button()
# bttn.pack()
# bttn.config(text="Button",command=button_action)

# entry = tk.Entry()
# entry.pack()

# window.mainloop()

import tkinter as tk

root = tk.Tk()
root.minsize(width=500,height=500)
root.title("My Grid Window")
root.config(padx=10,pady=10)

label = tk.Label(text="My Cute Label")
label.grid(column=0,row=0)

button = tk.Button()
button.config(text="Button")
button.grid(column=1,row=1)

new_button = tk.Button()
new_button.config(text="New Button")
new_button.grid(column=2,row=0)

entry = tk.Entry()
entry.grid(column=3,row=2)

tk.mainloop()