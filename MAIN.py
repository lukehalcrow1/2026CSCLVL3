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
root.title("Issue Tracker")
root.geometry("400x250")
root.resizable(False, False)

issue_var = tkinter.StringVar()
description_var = tkinter.StringVar()
location_var = tkinter.StringVar()
issue_var.trace("w", check_fields)
description_var.trace("w", check_fields)
location_var.trace("w", check_fields)

tkinter.Label(root, text="Issue").pack(pady=5)
issue_entry = tkinter.Entry(root, width=40, textvariable=issue_var)
issue_entry.pack()

tkinter.Label(root, text="Description").pack(pady=5)
description_entry = tkinter.Entry(root, width=40, textvariable=description_var)
description_entry.pack()

tkinter.Label(root, text="Location").pack(pady=5)
location_entry = tkinter.Entry(root, width=40, textvariable=location_var)
location_entry.pack()

save_button = tkinter.Button(root, text="Submit", command=save_data,
    state="disabled", bg="grey")
save_button.pack(pady=20)

root.mainloop()