import tkinter as tk
from tkinter import StringVar
import datetime
import pyttsx3
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def calculate_new_date():
    date_str = base_date_entry.get().strip()
    days_str = days_entry.get().strip()
    try:
        base_date = datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        delta_days = int(days_str)
        new_date = base_date + datetime.timedelta(days=delta_days)
        result = f"New Date: {new_date.strftime('%d-%m-%Y')}"
        result_var.set(result)
        copy_str.set(result)
        original_label.set(f"Original: {base_date.strftime('%d-%m-%Y')}")
        diff_label.set(f"Offset: {delta_days:+} days")
    except ValueError:
        result_var.set("❌ Invalid input! Format: dd-mm-yyyy & integer days")
        original_label.set("")
        diff_label.set("")

def speak_result():
    speak(result_var.get())

def copy_result():
    app.clipboard_clear()
    app.clipboard_append(copy_str.get())
    app.update()

def toggle_dark_mode():
    style.theme_use("darkly" if style.theme.name == "flatly" else "flatly")

app = ttk.Window(themename="flatly")
app.title("📆 Add/Subtract Days from Date")
app.geometry("750x550")  # ✅ Spacious window
app.resizable(False, False)

style = ttk.Style()

ttk.Label(app, text="📆 Add/Subtract Days from Date", font=("Segoe UI", 24, "bold")).pack(pady=20)

input_frame = ttk.Frame(app)
input_frame.pack(pady=15)

ttk.Label(input_frame, text="Enter Base Date (dd-mm-yyyy):", font=("Segoe UI", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
base_date_entry = ttk.Entry(input_frame, width=20, font=("Segoe UI", 12))
base_date_entry.grid(row=0, column=1, padx=10)

ttk.Label(input_frame, text="Days to Add/Subtract:", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
days_entry = ttk.Entry(input_frame, width=20, font=("Segoe UI", 12))
days_entry.grid(row=1, column=1, padx=10)

ttk.Button(app, text="➕➖ Calculate New Date", command=calculate_new_date, bootstyle=SUCCESS).pack(pady=10)

original_label = StringVar()
diff_label = StringVar()
result_var = StringVar()
copy_str = StringVar()

ttk.Label(app, textvariable=original_label, font=("Segoe UI", 11)).pack()
ttk.Label(app, textvariable=diff_label, font=("Segoe UI", 11)).pack()
ttk.Label(app, textvariable=result_var, font=("Segoe UI", 16)).pack(pady=10)

btn_frame = ttk.Frame(app)
btn_frame.pack(pady=30)

ttk.Button(btn_frame, text="🔊 Speak", command=speak_result, bootstyle=INFO).grid(row=0, column=0, padx=20)
ttk.Button(btn_frame, text="📋 Copy Result", command=copy_result, bootstyle=PRIMARY).grid(row=0, column=1, padx=20)
ttk.Button(btn_frame, text="🌓 Dark Mode", command=toggle_dark_mode, bootstyle=SECONDARY).grid(row=0, column=2, padx=20)

app.mainloop()
