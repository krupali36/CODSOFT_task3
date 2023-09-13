import tkinter as tk
import random
import string


# Function to generate a random password
def create_password():
    password_length = int(length_entry.get())

    # Define character sets for password
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on user's choice
    characters = ""
    if use_lowercase.get():
        characters += lower_case
    if use_uppercase.get():
        characters += upper_case
    if use_digits.get():
        characters += digits
    if use_special_chars.get():
        characters += special_chars

    if not characters:
        result_label.config(text="Please select at least one character set.")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_output.config(text="Generated Password: " + password)


# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("250x300+300+300")
window.config(background="#EEEEEE")
window.resizable(False, False)

# Label and Entry for password length
length_label = tk.Label(window, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Checkboxes for character sets
use_lowercase = tk.BooleanVar()
use_uppercase = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_special_chars = tk.BooleanVar()

lowercase_checkbox = tk.Checkbutton(window, text="Lowercase Letters", variable=use_lowercase)
uppercase_checkbox = tk.Checkbutton(window, text="Uppercase Letters", variable=use_uppercase)
digits_checkbox = tk.Checkbutton(window, text="Digits", variable=use_digits)
special_chars_checkbox = tk.Checkbutton(window, text="Special Characters", variable=use_special_chars)

lowercase_checkbox.pack()
uppercase_checkbox.pack()
digits_checkbox.pack()
special_chars_checkbox.pack()

# Button to generate password
generate_button = tk.Button(window, text="Generate Password", command=create_password)
generate_button.pack()

# Label to display the generated password
password_output = tk.Label(window, text="")
password_output.pack()

# Label to display error messages
result_label = tk.Label(window, text="", fg="red")
result_label.pack()

# Run the Tkinter main loop
window.mainloop()
