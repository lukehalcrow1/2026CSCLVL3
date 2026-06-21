import tkinter as tkinter
from tkinter import messagebox
import json
import os

datafile = "data.json"

data_dict = {}

def load_data():
    if os.path.exists(datafile):
        try:
            with open(datafile, "r" , encoding= "utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            messagebox.showerror("Error", "Failed to load data")
            return {}

def save_to_file():
    try:
        with open(datafile, "w", encoding="utf-8") as f:
            json.dump(data_dict, f, indent=4)
    except OSError:
        messagebox.showerror("Error", "Failed to save data")
        
def check_fields(*args):
    all_filled = (
        issue_var.get().strip() != "" and
        description_var.get().strip() != "" and
        location_var.get().strip() != ""
    )
    if all_filled:
        save_button.config(state="normal", bg="green")
    else:
        save_button.config(state="disabled", bg="grey")

def save_data():
    key = issue_var.get().strip()
    value1 = description_var.get().strip()
    value2 = location_var.get().strip()

    if key in data_dict:
        messagebox.showwarning("Duplicate Key", f"Issue '{key}' already exists")
        return

    data_dict[key] = {
        "Description": value1,
        "Location": value2
    }

    save_to_file()

    messagebox.showinfo("Saved", f"Data saved for '{key}'")


    issue_var.set("")
    description_var.set("")
    location_var.set("")


root = tkinter.Tk()
root.title("(Schoolname) Issue Reporting System")
root.geometry("400x800")
root.resizable(False, False)

issue_var = tkinter.StringVar()
description_var = tkinter.StringVar()
location_var = tkinter.StringVar()
issue_var.trace("w", check_fields)
description_var.trace("w", check_fields)
location_var.trace("w", check_fields)

instructions = tkinter.Label(root, text="This is the reporting system for (schoolname), Enter the name and a brief description of your issue, a location is also necessary for the resolution of the problem.",
font=("Arial", 10), wraplength=380, justify="center")
instructions.place(relx=0.5, rely=0.08, anchor="center")

tkinter.Label(root, text="Issue").place(relx=0.12, rely=0.25, anchor="w")
issue_entry = tkinter.Entry(root, width=40, textvariable=issue_var)
issue_entry.place(relx=0.5, rely=0.25, anchor="center")

tkinter.Label(root, text="Description").place(relx=0.035, rely=0.4, anchor="w")
description_entry = tkinter.Entry(root, width=40, textvariable=description_var)
description_entry.place(relx=0.5, rely=0.4, anchor="center")
 
tkinter.Label(root, text="Location").place(relx=0.07, rely=0.55, anchor="w")
location_entry = tkinter.Entry(root, width=40, textvariable=location_var)
location_entry.place(relx=0.5, rely=0.55, anchor="center")

save_button = tkinter.Button(root, text="Submit", command=save_data, state="disabled", bg="grey",width=20, height=4 )
save_button.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()