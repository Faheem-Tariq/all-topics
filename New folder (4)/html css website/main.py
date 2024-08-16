import tkinter as tk
from tkinter import *

# Create a window
window = tk.Tk()
window.title("Fast Food Restaurant")
window.geometry("400x400")

# Add labels
title_label = tk.Label(text="Welcome to Fast Food Restaurant", font=("Arial", 16))
title_label.pack()

item_label = tk.Label(text="Item", font=("Arial", 14))
item_label.pack()

price_label = tk.Label(text="Price", font=("Arial", 14))
price_label.pack()

# Create variables for item and price
item = StringVar()
price = StringVar()

# Create entry fields
item_entry = tk.Entry(textvariable=item)
item_entry.pack()

price_entry = tk.Entry(textvariable=price)
price_entry.pack()

# Add submit button
def submit_order():
    item_name = item.get()
    item_price = price.get()
    order = item_name + " - " + item_price + " dollars"
    order_label = tk.Label(text=order, font=("Arial", 14))
    order_label.pack()

submit_button = tk.Button(text="Submit", command=submit_order)
submit_button.pack()

# Run the window
window.mainloop()
