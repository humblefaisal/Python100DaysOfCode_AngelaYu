import tkinter as tk
from io import UnsupportedOperation
# import pandas as pd
import json
import random
from tkinter import messagebox
DATA_FILE = "./db/info.json" 



# password generate logic
def generate_password():
    global entry_password,root
    length=15
    num_letter = 8
    num_symbols = 4
    num_digits = 3

    password = []

    for i in range(0,num_letter):
        character_case = random.randint(0,1)
        letter = chr((1-character_case)*random.randint(65,90)+character_case*random.randint(97,122))
        password.append(letter) 
    for i in range(0,num_symbols) :
        symbol = chr(random.randint(33,47))
        password.append(symbol)
    for i in range(0,num_digits):
        number = chr(random.randint(48,57))
        password.append(number)
    for i in range(0,num_digits+num_letter+num_symbols) :
        index = random.randint(0,num_digits+num_letter+num_symbols-1)
        temp = password[i]
        password[i] = password[index]
        password[index] = temp
    random.shuffle(password)
    password_str = "".join(password)
    entry_password.delete(0,tk.END)
    entry_password.insert(0,string=password_str)
    root.clipboard_clear()
    root.clipboard_append(password_str)
    root.update()

# save oassword info logic
def addinfo():
    global entry_password,entry_user,entry_website
    password = entry_password.get()
    user = entry_user.get()
    website = entry_website.get()

    if password=="" or user=="" or website=="" :
        messagebox.showwarning(title="Oops!",message="Please dont leave too many fields empty!")
        return
    is_ok = messagebox.askokcancel(title=website,message=f"Your details are:\nEmail:{user}\npassword:{password}")
    if(not is_ok) :
        messagebox.showinfo(title="Canceled Operation!",message="Your detials have not been saved.")
        return
    entry_password.delete(0,tk.END)
    entry_website.delete(0,tk.END)
    entry_website.focus()
    try:
        with open(DATA_FILE,mode="r") as data_file:
            data = json.load(data_file) 
        data[website].append({
            "Email" : user,
            "Password" : password
        })
        with open(DATA_FILE,mode="w") as data_file_write: 
            json.dump(data,data_file_write,indent=4)
    except FileNotFoundError or UnsupportedOperation:
        print("FileNotFoundError")

        with open(DATA_FILE,mode="w") as data_file_write: 
            data = {
                website : [{
                    "Email" : user,
                    "Password":password
                }]
            }
            json.dump(data,data_file_write,indent=4)
    except KeyError:
        print("KeyError")
        data[website] = [{
            "Email" : user,
            "Password":password
        }]
        with open(DATA_FILE,mode="w") as data_file_write:
            json.dump(data,data_file_write,indent=4)
    messagebox.showinfo(title="Success!",message="Your detials have been successfully saved.")

    
def search():
    global  entry_website,entry_user
    website = entry_website.get()
    email = entry_user.get()
    info = {
        "Website":website,
        "Email":email,
        "Password":""
    }
    with open("./db/info.json",mode="r") as file:
        db = json.load(file)
    try :     
        user_pass_list = db[website]
        for user_pass in user_pass_list:
            if user_pass["Email"] == email:
                info["Password"]=user_pass["Password"]
                break
        if info["Password"] == "" : 
            raise LookupError("No passwords stored for this website/email combo")
    except KeyError:
        messagebox.showerror(title=f"{website}",message=f"No info stored for {website}")
    except LookupError:
        messagebox.showerror(f"No passwords stored for this {website}-{email} combo")
    else:
        messagebox.showinfo(title="Details",message=f"website : {info["Website"]}\nEmail : {info["Email"]}\nPassword : {info['Password']}")
        root.clipboard_clear()
        root.clipboard_append(info["Password"])
        root.update()



root = tk.Tk()
root.minsize(width=240,height=240)
root.config(padx=60,pady=60)

logo_frame = tk.Frame(master=root)
logo_frame.grid(column=1,row=0)

password_info_frame = tk.Frame(master=root)
password_info_frame.grid(column=0,columnspan=3,row=1)

canvas = tk.Canvas(master=logo_frame,width=200,height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(0,0,image=logo_img,anchor="nw")
canvas.pack()

label_website = tk.Label(master=password_info_frame,text="Website:")
label_website.grid(row=0,column=0)
label_user = tk.Label(master=password_info_frame,text="Email/Username:")
label_user.grid(row=1,column=0)
label_password = tk.Label(master=password_info_frame,text="Password:")
label_password.grid(row=2,column=0)

entry_website = tk.Entry(master=password_info_frame,width=21)
entry_website.focus()
entry_website.grid(column=1,columnspan=1,row=0,sticky="w")
entry_user = tk.Entry(master=password_info_frame,width=42)
entry_user.insert(index=0,string="mdfaisalaftab2004@gmail.com")
entry_user.grid(column=1,columnspan=2,row=1,sticky="w")
entry_password = tk.Entry(master=password_info_frame,width=21)
entry_password.grid(column=1,columnspan=1,row=2,sticky="w")

button_generate_password = tk.Button(master=password_info_frame,width=15,text="Generate Password",command=generate_password) 
button_generate_password.grid(column=2,columnspan=1,row=2)
button_addinfo = tk.Button(master=password_info_frame,width=36,text="Add",command=addinfo)
button_addinfo.grid(column=1,columnspan=2,row=3,sticky="w")
button_search = tk.Button(master=password_info_frame,width=15,text="Search",command=search)
button_search.grid(column=2,row=0,sticky="w")


root.mainloop()