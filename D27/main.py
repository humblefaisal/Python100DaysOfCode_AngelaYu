import tkinter as tk


root = tk.Tk()
root.title("Miles to KM Converter")
root.minsize(width=300,height=300)
root.config(padx=10,pady=10)

miles_entry = tk.Entry()
miles_entry.insert(tk.END,"1")
miles_entry.grid(column=1,row=0,padx=10,pady=10)

miles_label = tk.Label(text="Miles")
miles_label.config(padx=10,pady=10)
miles_label.grid(column=2,row=0)

label = tk.Label(text="equals to : ")
label.config(padx=10,pady=10)
label.grid(column=0,row=1)

km_value_label = tk.Label(text="1.61")
km_value_label.config(padx=10,pady=10)
km_value_label.grid(column=1,row=1)

km_label = tk.Label(text="Km")
km_label.config(padx=10,pady=10)
km_label.grid(column=2,row=1)
def action():
    km_value_label.config(text=f"{1.61*int(miles_entry.get()):.2f}")
calculate_bttn = tk.Button(text="Calculate",padx=10,pady=10,command=action)
calculate_bttn.grid(column=1,row=2)

root.mainloop()




