import tkinter as tk
from tkinter import messagebox

data_dict = {}

def save_data():
    key = entry1.get()
    value1 = entry2.get()
    value2 = entry3.get()

    data_dict[key] = {
        "Issue": value1,
        "Location": value2
    }

    messagebox.showinfo("Saved", f"saved for '{key}'")

    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)

    print(data_dict)

root = tk.Tk()
root.title("issue")
root.geometry("400x250")

tk.Label(root, text="issue").pack(pady=5)
entry1 = tk.Entry(root, width=40)
entry1.pack()

tk.Label(root, text="issue").pack(pady=5)
entry2 = tk.Entry(root, width=40)
entry2.pack()

tk.Label(root, text="where").pack(pady=5)
entry3 = tk.Entry(root, width=40)
entry3.pack()

save_button = tk.Button(root, text="submit", command=save_data)
save_button.pack(pady=20)

root.mainloop()