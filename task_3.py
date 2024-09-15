import tkinter as tk  # Import the tkinter module for GUI
from tkinter import messagebox  # Import messagebox for error messages
import random  # Import random for generating random characters
import string  # Import string for character sets

def generate_password(length):
    # Function to generate a random password of a given length
    if length < 1:  # Check if the length is less than 1
        return ""  # Return an empty string if invalid
    
    # Define the characters to use: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by selecting random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password  # Return the generated password

def on_generate_button_click():
    # Function to handle the button click event
    try:
        length = int(entry_length.get())  # Get the length from the entry widget and convert it to an integer
        if length <= 0:  # Check if the length is less than or equal to 0
            raise ValueError  # Raise an exception if invalid
        password = generate_password(length)  # Generate the password
        # Update the result button with the generated password and a message
        button_result.config(text=f"Generated Password: {password}\nGreat, visit again!", command=lambda: None)
    except ValueError:  # Handle invalid input
        # Show an error message if the input is not a positive integer
        messagebox.showerror("Invalid Input", "Please enter a positive integer for the length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")  # Set the title of the window

# Set the window size
root.geometry("800x600")

# Set the background color of the window
root.configure(bg="light pink")

# Create and place the header label at the top
header_label = tk.Label(root, text="Aryan Yadav @ Password Generator", 
                       font=("Helvetica", 24, "italic"), fg="yellow", bg="black")
header_label.pack(fill=tk.X, pady=20)  # Fill the X-axis and add vertical padding

# Create and place a label prompting the user to enter the password length
tk.Label(root, text="Enter the length of the password:", 
         font=("Helvetica", 14), fg="dark blue", bg="light pink").pack(pady=10)

# Create and place an entry widget for the user to input the desired password length
entry_length = tk.Entry(root, font=("Helvetica", 14))
entry_length.pack(pady=5)  # Add vertical padding

# Create and place a button to generate the password
tk.Button(root, text="Generate Password", command=on_generate_button_click, 
          font=("Helvetica", 16), bg="light blue", fg="black", height=2, width=20).pack(pady=20)

# Create and place a button to display the result
button_result = tk.Button(root, text="", font=("Helvetica", 16), bg="green", fg="white", 
                          height=4, width=50, command=lambda: None)
button_result.pack(pady=20)  # Add vertical padding

# Start the Tkinter event loop
root.mainloop()
