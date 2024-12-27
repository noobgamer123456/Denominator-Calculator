import tkinter as tk
import re

def check_password_strength():
    password = password_entry.get()
    length_criteria = len(password) >=8
    digit_criteria = bool(re.search(r"\d",password))
    uppercase_criteria = bool(re.search(r"[A-Z]",password))
    lowercase_criteria = bool(re.search(r"[a-z]",password))
    
    symbol_criteria = bool(re.search(r"[@#$%&(){};:.,/\~^_+=!?<>*]",password))
    
    criteria_met = sum([length_criteria,digit_criteria,uppercase_criteria,lowercase_criteria,symbol_criteria])
    
    if criteria_met <=2:
        strength = "Weak"
    elif criteria_met ==3 or criteria_met == 4:
        strength = "Medium"
    else:
        strength = "Strong"
    result_label.config(text=f"Password Strength:{strength}")
    
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x300")

password_label = tk.Label(root,text = "Enter Password")
password_label.pack(pady=5)

password_entry = tk.Entry(root)
password_entry.pack(pady=5)

check_button = tk.Button(root,text = "Check Strength",command=check_password_strength)
check_button.pack(pady=10)

result_label = tk.Label(root,text= "")
result_label.pack(pady=10)

root.mainloop()