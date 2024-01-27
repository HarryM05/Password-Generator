import tkinter as tk
from tkinter import scrolledtext
import string, random

root = tk.Tk()

class PasswordGenerator:
    def generate_password(self):
        #Clear textbox
        self.password_text.delete(1.0, tk.END)

        #Get character sets specified by the user
        characters = ""
        if self.uppercase_var.get():
            characters += string.ascii_uppercase

        if self.lowercase_var.get():
            characters += string.ascii_lowercase

        if self.digits_var.get():
            characters += string.digits

        if self.special_chars_var.get():
            characters += string.punctuation

        #Set other qualities
        password_length = self.slider_value.get()
        password_amount = self.dropdown_value.get()

        #Generate passwords
        passwords = [''.join(random.choice(characters) for _ in range(password_length)) for _ in range(password_amount)]

        #Display passwords on separate lines
        for i, password in enumerate(passwords):
            self.password_text.insert(tk.END, f"Password {i+1}:\n {password}\n")

    def user_interface(self):
        #Create main window
        root.title("Password Generator")
        root.geometry("500x600")
        root.configure(bg="#3498db")

        #Variables for checkboxes
        self.uppercase_var = tk.BooleanVar()
        self.lowercase_var = tk.BooleanVar()
        self.digits_var = tk.BooleanVar()
        self.special_chars_var = tk.BooleanVar()

        #Create checkboxes
        tk.Checkbutton(root, text="Uppercase", variable=self.uppercase_var, bg="#3498db", font=("Arial", 12)).pack()
        tk.Checkbutton(root, text="Lowercase", variable=self.lowercase_var, bg="#3498db", font=("Arial", 12)).pack()
        tk.Checkbutton(root, text="Digits", variable=self.digits_var, bg="#3498db", font=("Arial", 12)).pack()
        tk.Checkbutton(root, text="Special Characters", variable=self.special_chars_var, bg="#3498db", font=("Arial", 12)).pack()

        #Create a button to generate password
        generate_btn = tk.Button(root, text="Generate Password", width=20, bg="#2ecc71", fg="white", font=("Arial", 12), command=self.generate_password)
        generate_btn.pack(pady=10)

        #Create a slider for password length
        self.slider_value = tk.IntVar()
        tk.Scale(root, variable=self.slider_value, from_=8, to=30, orient=tk.HORIZONTAL, label="Password Length", length=400).pack(pady=10)

        #Create a dropdown for amount of passwords
        self.dropdown_value = tk.IntVar(value=1)
        tk.Label(root, text="Number of Passwords:", font=("Arial", 12), bg="#3498db").pack()
        tk.OptionMenu(root, self.dropdown_value, *range(1, 6)).pack(pady=10)

        #Create a textbox to display generated passwords
        self.password_text = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD, font=("Arial", 12))
        self.password_text.insert(tk.INSERT, "Generated Passwords Appear Here\n")
        self.password_text.pack(pady=10)

password_generator = PasswordGenerator()
password_generator.user_interface()
root.mainloop()