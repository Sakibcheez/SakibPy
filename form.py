import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    gender = gender_var.get()

    if not name or not email or not gender:
        messagebox.showwarning("Incomplete", "Please fill all fields.")
    else:
        # Save to a text file
        with open("form_data.txt", "a") as file:
            file.write(f"Name: {name}, Email: {email}, Gender: {gender}\n")

        messagebox.showinfo("Submitted", "Form submitted and saved successfully!")

        # Clear fields after submission
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        gender_var.set(None)

# Main window
root = tk.Tk()
root.title("Simple Form")
root.geometry("300x300")

# Name
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

# Email
tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()

# Gender
tk.Label(root, text="Gender:").pack(pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()
