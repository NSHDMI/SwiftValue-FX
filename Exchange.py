import requests
import os
import tkinter as tk
from tkinter import messagebox
import threading
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

def start_convert():
    # Run network request in a separate thread to keep the UI responsive
    label_result.config(text="⏳ Fetching data...", fg="#2196F3")
    btn.config(state="disabled") 
    
    thread = threading.Thread(target=do_conversion)
    thread.daemon = True
    thread.start()

def do_conversion():
    from_curr = entry_currency.get().upper().strip()
    to_curr = entry_to.get().upper().strip()
    amount_str = entry_amount.get().strip()

    # Basic input validation
    if not from_curr or not to_curr or not amount_str:
        label_result.config(text="❌ Please fill all fields", fg="#f44336")
        btn.config(state="normal")
        return

    try:
        amount = float(amount_str)
        if amount <= 0:
            label_result.config(text="❌ Enter a positive number", fg="#f44336")
            btn.config(state="normal")
            return
    except ValueError:
        label_result.config(text="❌ Invalid amount format", fg="#f44336")
        btn.config(state="normal")
        return

    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_curr}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get('result') == 'error':
            error_type = data.get('error-type', 'unknown')
            label_result.config(text=f"❌ API Error: {error_type}", fg="#f44336")
            btn.config(state="normal")
            return

        rates = data.get('conversion_rates', {})
        rate = rates.get(to_curr)

        if rate:
            total = amount * rate
            label_result.config(text=f"✅ {amount:,.2f} {from_curr} = {total:,.2f} {to_curr}", fg="#5CDF60")
            label_info.config(text=f"Rate: 1 {from_curr} = {rate:.4f} {to_curr}", fg="#fff")
        else:
            label_result.config(text=f"❌ Currency {to_curr} not found", fg="#f44336")
            label_info.config(text="")

    except Exception as e:
        label_result.config(text="❌ Connection error", fg="#f44336")
    finally:
        # Always re-enable the button
        btn.config(state="normal")

def clear_fields():
    entry_currency.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_to.delete(0, tk.END)
    label_result.config(text="Enter data and press 'Convert'", fg="#fff")
    label_info.config(text="")

def show_help():
    popular = "Common codes: USD, EUR, GBP, JPY, CNY, RUB, UAH, TRY, CHF, CAD"
    messagebox.showinfo("Supported Currencies", popular)


# UI Setup
current_dir = os.path.dirname(os.path.abspath(__file__))
root = tk.Tk()
icon_img = tk.PhotoImage(file=os.path.join(current_dir, "icon.png"))
root.iconphoto(False, icon_img)
root.title("Currency Converter")
root.geometry("500x450")
root.configure(bg="#333333")
root.resizable(False, False)

# Header
title_frame = tk.Frame(root, bg="#697B8A", height=60)
title_frame.pack(fill="x")
tk.Label(title_frame, text="SwiftValue", font=("Arial", 20, "bold"), bg="#697B8A", fg="white").pack(pady=15)

main_frame = tk.Frame(root, bg="#333333")
main_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Input area
input_frame = tk.Frame(main_frame, bg="#939CA3", relief="solid", bd=1)
input_frame.pack(pady=10, padx=10, fill="x")

# Grid layout for inputs
tk.Label(input_frame, text="From:", bg="#939CA3").grid(row=0, column=0, sticky="e", padx=15, pady=10)
entry_currency = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry_currency.grid(row=0, column=1, padx=15, pady=10)

tk.Label(input_frame, text="Amount:", bg="#939CA3").grid(row=1, column=0, sticky="e", padx=15, pady=10)
entry_amount = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry_amount.grid(row=1, column=1, padx=200, pady=10)

tk.Label(input_frame, text="To:", bg="#939CA3").grid(row=2, column=0, sticky="e", padx=15, pady=10)
entry_to = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry_to.grid(row=2, column=1, padx=15, pady=10)

# Buttons
btn_frame = tk.Frame(main_frame, bg="#333333")
btn_frame.pack(pady=15)

btn = tk.Button(btn_frame, text="Convert", bg="#568057", fg="white", width=12, command=start_convert)
btn.grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="Clear", bg="#d19b49", fg="white", width=12, command=clear_fields).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Help", bg="#4D84B1", fg="white", width=12, command=show_help).grid(row=0, column=2, padx=5)

# Result display
result_frame = tk.Frame(main_frame, bg="#697B8A", relief="solid", bd=1, height=80)
result_frame.pack(pady=10, padx=10, fill="x")
result_frame.pack_propagate(False)

label_result = tk.Label(result_frame, text="Waiting for input...", font=("Arial", 11, "bold"), bg="#697B8A", fg="#fff")
label_result.pack(pady=10)
label_info = tk.Label(result_frame, text="", font=("Arial", 9), bg="#697B8A", fg="#666")
label_info.pack()



# Start
entry_currency.focus()
root.bind('<Return>', lambda e: start_convert())
root.mainloop()