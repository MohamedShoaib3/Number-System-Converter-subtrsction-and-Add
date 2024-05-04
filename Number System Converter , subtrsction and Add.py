import tkinter as tk
from tkinter import messagebox

def add_to_entry(number):
    current_text = ""
    if active_entry == 1:
        current_text = entry_num1.get()
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, current_text + str(number))
    elif active_entry == 2:
        current_text = entry_num2.get()
        entry_num2.delete(0, tk.END)
        entry_num2.insert(0, current_text + str(number))

def clear_entry():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)

def convert(operation):
    num1 = entry_num1.get().strip()
    num2 = entry_num2.get().strip()

    if not num1 and not num2:
        messagebox.showerror("Error", "Please enter a number in at least one field.")
        return

    from_base1 = from_base_var1.get()
    from_base2 = from_base_var2.get()
    to_base = to_base_var.get()

    try:
        # Convert numbers to decimal if they are not empty
        decimal_num1 = int(num1, from_base1) if num1 else 0
        decimal_num2 = int(num2, from_base2) if num2 else 0

        # Perform addition or subtraction
        if operation == "add":
            result_decimal = decimal_num1 + decimal_num2
        elif operation == "subtract":
            result_decimal = decimal_num1 - decimal_num2

        # Convert result to the desired base
        if to_base == 2:
            result = bin(result_decimal)[2:]
        elif to_base == 8:
            result = oct(result_decimal)[2:]
        elif to_base == 10:
            result = str(result_decimal)
        elif to_base == 16:
            result = hex(result_decimal)[2:].upper()

        # Update the result label
        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Invalid input")

custom_font = ("Arial", 13, "bold")        

# Create main window
root = tk.Tk()
root.title("Number System Converter")
root.configure(bg="#293854")  # Setting background color for the root window

# Labels and entry fields for entering numbers
tk.Label(root, text="Number 1:", bg="#293854", fg="white", font =custom_font).grid(row=0, column=0, pady=5, sticky="e")
entry_num1 = tk.Entry(root)
entry_num1.configure(bg="#293854", fg="white", font =custom_font)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Base:", bg="#293854", fg="#FF355E", font =custom_font).grid(row=0, column=2, pady=5, sticky="e")
from_base_var1 = tk.IntVar(root)
from_base_var1.set(10)
from_base_menu1 = tk.OptionMenu(root, from_base_var1, 2, 8, 10, 16)
from_base_menu1.configure(bg="#293854",fg="white", font =custom_font)
from_base_menu1.grid(row=0, column=3, padx=5, pady=5)

tk.Label(root, text="Number 2:",bg="#293854" , fg="white", font =custom_font).grid(row=1, column=0, pady=5, sticky="e")
entry_num2 = tk.Entry(root)
entry_num2.configure(bg="#293854", fg="white", font =custom_font)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Base:", bg="#293854", fg="#FF355E", font =custom_font).grid(row=1, column=2, pady=5, sticky="e")
from_base_var2 = tk.IntVar(root)
from_base_var2.set(10)
from_base_menu2 = tk.OptionMenu(root, from_base_var2, 2, 8, 10, 16)
from_base_menu2.configure(bg="#293854",fg="white", font =custom_font)
from_base_menu2.grid(row=1, column=3, padx=5, pady=5)

# Track which entry is active
active_entry = 1

# Function to switch active entry
def switch_active_entry(entry):
    global active_entry
    active_entry = entry
    
def free_palestine():
    messagebox.showinfo("Free Palestine", "Solidarity with Palestine!")

# Bindings to switch active entry
entry_num1.bind("<FocusIn>", lambda event: switch_active_entry(1))
entry_num2.bind("<FocusIn>", lambda event: switch_active_entry(2))

# Clear button
tk.Button(root, text="C", command=clear_entry, bg="#34476B", fg="#FF355E", font =custom_font,width=7, height=3).grid(row=5, column=1, columnspan=4, padx=5, pady=5, sticky="ew")

# Add and Subtract buttons
tk.Button(root, text="Add", command=lambda: convert("add"), bg="#34476B", fg="#FF355E", font =custom_font,width=7, height=3).grid(row=6, column=0, padx=5, pady=5, sticky="ew")
tk.Button(root, text="Subtract", command=lambda: convert("subtract"), bg="#34476B", fg="#FF355E", font =custom_font,width=7, height=3).grid(row=6, column=1, padx=5, pady=5, sticky="ew")

tk.Button(root, text="Free Palestine", command=free_palestine,bg="#293854", fg="#FFC53A", font =custom_font).grid(row=8, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

# Convert button
tk.Button(root, text="Convert", command=lambda: convert("add"), bg="#FF355E", fg="white", font =custom_font,width=7, height=3).grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

# Result label
tk.Label(root, text="Result:",   bg="#293854", fg="white", font =custom_font).grid(row=7, column=0, pady=5, sticky="e")
result_label = tk.Label(root, text="", bg="white", font =custom_font, relief="ridge", width=20)
result_label.configure(bg="#293854", fg="white", font =custom_font)
result_label.grid(row=7, column=1, padx=5, pady=5, columnspan=3, sticky="ew")

# Convert to base label
tk.Label(root, text="Convert To:",  bg="#293854", fg="#FF355E", font =custom_font).grid(row=8, column=0, pady=5, sticky="e")
to_base_var = tk.IntVar(root)
to_base_var.set(10)
to_base_menu = tk.OptionMenu(root, to_base_var, 2, 8, 10, 16,)
to_base_menu.configure(bg="#293854", fg="white", activebackground="#293854", font =custom_font)
to_base_menu.grid(row=8, column=1, padx=5, pady=5)




# Number buttons
numbers = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0']
row = 2
col = 0

for number in numbers:
    tk.Button(root, text=number, command=lambda num=number: add_to_entry(num), bg="#293854", fg="white", font =custom_font, width=7, height=3).grid(row=row, column=col, padx=6, pady=6)
    col += 1
    if col > 2:
        col = 0
        row += 1


root.mainloop()