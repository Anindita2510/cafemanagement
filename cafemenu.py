import tkinter as tk
from tkinter import messagebox

# Menu dictionary
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80,
}

# Initialize total
order_total = 0
ordered_items = []

# Function to add selected item
def add_item():
    global order_total
    selected_item = item_var.get()
    if selected_item in menu:
        order_total += menu[selected_item]
        ordered_items.append(selected_item)
        result_label.config(text=f"{selected_item} added. Current total: Rs {order_total}")
    else:
        messagebox.showerror("Item Not Available", f"Sorry, {selected_item} is not on the menu.")

# Function to show final bill
def show_total():
    if ordered_items:
        item_list = ", ".join(ordered_items)
        messagebox.showinfo("Total Bill", f"You ordered: {item_list}\nTotal amount: Rs {order_total}")
    else:
        messagebox.showinfo("No Order", "You haven't ordered anything yet.")

# Set up the main window
root = tk.Tk()
root.title("PYTHON Restaurant")
root.geometry("400x300")

# Greeting label
greet = tk.Label(root, text="Welcome to PYTHON Restaurant", font=("Arial", 16))
greet.pack(pady=10)

# Dropdown for items
item_var = tk.StringVar(root)
item_var.set("Pizza")  # default value
item_menu = tk.OptionMenu(root, item_var, *menu.keys())
item_menu.pack(pady=5)

# Add item button
add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=5)

# Show total button
total_button = tk.Button(root, text="Show Total", command=show_total)
total_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the app
root.mainloop()