# Import Module
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")


total_frame = tk.Frame(root)
total_frame.pack(pady=10)

accounts_frame = tk.Frame(root)
accounts_frame.pack(pady=20)

accounts = []

# Lable/Entry for the Total ammount
total_label = tk.Label(total_frame, text="Total")
total_label.grid(row=0, column=0)
total_entry = tk.Entry(total_frame, width=20)
total_entry.grid(row=0, column=1)


def open_add_account():
    top = tk.Toplevel(root)
    top.title('Add Account')
    top.geometry('400x400')
    top.focus_set()

    # Account Name
    name_label = tk.Label(top, text="Account Name:")
    name_label.grid(row=0, column=0, pady=5)
    name_entry = tk.Entry(top)
    name_entry.grid(row=0, column=1, pady=5)
    name_entry.focus()

    # Radio button for Fixed / Percent
    var_type = tk.StringVar(value="fixed")  # Default is Fixed
    fixed_rb = tk.Radiobutton(top, text="Fixed", variable=var_type,
                              value="fixed")
    fixed_rb.grid(row=1, column=0)
    fixed_entry = tk.Entry(top)
    fixed_entry.grid(row=1, column=1)

    percent_rb = tk.Radiobutton(top, text="Percent", variable=var_type,
                                value="percent")
    percent_rb.grid(row=2, column=0)
    percent_entry = tk.Entry(top)
    percent_entry.grid(row=2, column=1)

    def create_account():
        name = name_entry.get()
        acc_type = var_type.get()

        if acc_type == "fixed":
            value = fixed_entry.get()

        else:
            value = percent_entry.get()

        

        if not name:
            error_message = tk.Message(top, text='Please enter a Valid Name',
                                       width=200)
            error_message.grid(row=4, column=1, pady=5)
        else:
            add_account(name, acc_type, value)
            

    def close_popup():
        top.destroy()

    create_button = tk.Button(top, text="Create", command=create_account)
    create_button.grid(row=3, column=0, pady=5)

    done_button = tk.Button(top, text="Done", command=close_popup)
    done_button.grid(row=3, column=1, pady=5)

    def update_entry():
        if var_type.get() == "fixed":
            percent_entry.config(state=tk.DISABLED)
            percent_entry.delete(0, tk.END)
            fixed_entry.config(state=tk.NORMAL)
        else:
            fixed_entry.config(state=tk.DISABLED)
            fixed_entry.delete(0, tk.END)
            percent_entry.config(state=tk.NORMAL)

    update_entry()

    fixed_rb.config(command=update_entry)
    percent_rb.config(command=update_entry)


def add_account(name="New Account", var_type="fixed", entry="entry"):
    if var_type is None:
        var_type = tk.StringVar(value="fixed")

    row = len(accounts)  # Read the next line

    # To-Do add a message box, so when user add account, it will ask for the 
    # name. update the label

    # Account name label
    label = tk.Label(accounts_frame, text=name)
    label.grid(row=row, column=0)

    # Entry widget for ammount
    entry = tk.Entry(accounts_frame, width=10)
    entry.grid(row=row, column=1)

    percent_entry = tk.Entry(accounts_frame, width=10)
    percent_entry.grid(row=row, column=3)

    percent_label = tk.Label(accounts_frame, text="%")
    percent_label.grid(row=row, column=4)

    account = {
            "name": name,
            "entry": entry,
            "label": label,
            "var_type": var_type,
            "percent_entry":  percent_entry
        }  
    accounts.append(account)


add_button = tk.Button(root, text="Add Account", command=open_add_account)
add_button.pack()


def calculate():
    total = float(total_entry.get())
    remaining = total

    # Subtract fixed amount
    for acc in accounts:
        if acc["var_type"].get() == "fixed":
            remaining = remaining - float(acc["entry"].get())

    # Calculate percent amount
    for acc in accounts:
        if acc["var_type"].get() == "percent":
            acc_amount = remaining * float(acc["percent_entry"].get()) / 100
            # Update the account entry
            acc["entry"].delete(0, tk.END)
            acc["entry"].insert(0, str(acc_amount))


calculate_button = tk.Button(total_frame, text="Calculate", command=calculate)
calculate_button.grid(row=0, column=2)

# To-Do add a rename function. it will get the old name and ask user for the 
# new name. it will then update the label
# add button

# To-Do add a delete function. it will delete the entry  from the dictionary
# add button

# To-Do add a sub account functiion. it will create a sub account for the main 
# accounts
# create frame, label, entry radio buttons for fixd and percentage
# add button

# Execute Tkinter
root.mainloop()