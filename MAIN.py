rom tkinter import messagebox

data_dict = {}

def check_fields(*args): 
    all_filled = (
        entry1.get().strip() != "" and
        entry2.get().strip() != "" and
        entry3.get().strip() != ""
    )
    if all_filled:
        save_button.config(state="normal", bg="green")
    else:
        save_button.config(state="disabled", bg="grey")

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
root.resizable(False, False)  

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var1.trace("w", check_fields)  
var2.trace("w", check_fields)
var3.trace("w", check_fields)

tk.Label(root, text="issue").pack(pady=5)
entry1 = tk.Entry(root, width=40, textvariable=var1) 
entry1.pack()

tk.Label(root, text="issue").pack(pady=5)
entry2 = tk.Entry(root, width=40, textvariable=var2) 
entry2.pack()

tk.Label(root, text="where").pack(pady=5)
entry3 = tk.Entry(root, width=40, textvariable=var3)  
entry3.pack()

save_button = tk.Button(root, text="submit", command=save_data,
    state="disabled", bg="grey") 
save_button.pack(pady=20)

root.mainloop()