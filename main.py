import tkinter as tk
from tkinter import ttk

# Simple currency rates (example rates)
rates = {
    "INR": 1,
    "USD": 0.012,
    "JPY": 1.78,
    "GBP": 0.0095,
    "CNY": 0.087
}

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_box.get()
    to_currency = to_box.get()

    # Convert to INR first
    inr_amount = amount / rates[from_currency]

    # Convert INR to target currency
    result = inr_amount * rates[to_currency]

    result_label.config(text=f"Converted Amount: {round(result,2)} {to_currency}")

# Window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x300")

# Amount
tk.Label(root, text="Enter Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# Currency list
currencies = ["INR", "USD", "JPY", "GBP", "CNY"]

# From Currency
tk.Label(root, text="From Currency").pack()
from_box = ttk.Combobox(root, values=currencies)
from_box.pack()

# To Currency
tk.Label(root, text="To Currency").pack()
to_box = ttk.Combobox(root, values=currencies)
to_box.pack()

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=convert_currency)
convert_btn.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()