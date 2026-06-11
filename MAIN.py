import tkinter as tkinter
from tkinter import messagebox


data_dict = {}


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
        messagebox.showwarning("Duplicate Key", f"Issue '{key}' already exists!")
        return

    data_dict[key] = {
        "Description": value1,
        "Location": value2
    }

    messagebox.showinfo("Saved", f"Data saved for '{key}'")


    issue_var.set("")
    description_var.set("")
    location_var.set("")

    print(data_dict)

root = tkinter.Tk()
root.title("(Schoolname) Issue Reporting System")
root.geometry("400x700")
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

tkinter.Label(root, text="Issue").place(relx=0.12, rely=0.2, anchor="w")
issue_entry = tkinter.Entry(root, width=40, textvariable=issue_var)
issue_entry.place(relx=0.5, rely=0.2, anchor="center")

tkinter.Label(root, text="Description").place(relx=0.035, rely=0.35, anchor="w")
description_entry = tkinter.Entry(root, width=40, textvariable=description_var)
description_entry.place(relx=0.5, rely=0.35, anchor="center")

tkinter.Label(root, text="Location").place(relx=0.07, rely=0.5, anchor="w")
location_entry = tkinter.Entry(root, width=40, textvariable=location_var)
location_entry.place(relx=0.5, rely=0.5, anchor="center")

save_button = tkinter.Button(root, text="Submit", command=save_data, state="disabled", bg="grey")
save_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()