import tkinter as tk  # Import tkinter for creating the graphical interface
from tkinter import messagebox  # Import messagebox for showing messages
import random  # Import random for making random choices
import time  # Import time for showing the current time

def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"  # Return tie if both choices are the same
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"  # Return win if user's choice beats computer's choice
    else:
        return "You lose!"  # Return lose if computer's choice beats user's choice

def make_choice(user_choice):
    """Handle button clicks and update game results."""
    choices = ['rock', 'paper', 'scissors']  # List of choices
    computer_choice = random.choice(choices)  # Computer picks a random choice
    
    result = determine_winner(user_choice, computer_choice)  # Determine the result of the game
    
    # Update scores based on the result
    global user_score, computer_score, ties
    if result == "You win!":
        user_score += 1  # Increase user's score if they win
    elif result == "You lose!":
        computer_score += 1  # Increase computer's score if user loses
    else:
        ties += 1  # Increase ties count if it's a tie
    
    # Update labels to show the results and scores
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score} - Ties {ties}")

def update_time():
    """Update the time display."""
    current_time = time.strftime("%M:%S")  # Get the current time in minutes and seconds
    time_label.config(text=f"Time: {current_time}")  # Update the time label with current time
    root.after(1000, update_time)  # Call this function again after 1 second to update time

# Create the main window
root = tk.Tk()  # Create a new Tkinter window
root.title("Rock Paper Scissors")  # Set the title of the window
root.geometry("800x600")  # Set the size of the window to 800x600 pixels
root.config(bg="light pink")  # Set the background color of the window to light pink

# Initialize scores
user_score = 0  # Initialize user's score to 0
computer_score = 0  # Initialize computer's score to 0
ties = 0  # Initialize ties count to 0

# Create and place widgets
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 24), bg="light pink")
title_label.pack(pady=20)  # Place the title label with padding

# Center text
center_label = tk.Label(root, text="Aryan Yadav - Task", font=("Helvetica", 18, "bold"), bg="light pink")
center_label.pack(pady=20)  # Place the center label with padding

# Buttons with colors
rock_button = tk.Button(root, text="Rock", command=lambda: make_choice('rock'), bg="red", fg="white", width=15)
rock_button.pack(side=tk.TOP, padx=10, pady=10)  # Place the rock button at the top with padding

paper_button = tk.Button(root, text="Paper", command=lambda: make_choice('paper'), bg="green", fg="white", width=15)
paper_button.pack(side=tk.TOP, padx=10, pady=10)  # Place the paper button at the top with padding

scissors_button = tk.Button(root, text="Scissors", command=lambda: make_choice('scissors'), bg="blue", fg="white", width=15)
scissors_button.pack(side=tk.TOP, padx=10, pady=10)  # Place the scissors button at the top with padding

extra_button1 = tk.Button(root, text="Extra1", command=lambda: None, bg="orange", fg="white", width=15)
extra_button1.pack(side=tk.TOP, padx=10, pady=10)  # Place an extra button with orange color

extra_button2 = tk.Button(root, text="Extra2", command=lambda: None, bg="purple", fg="white", width=15)
extra_button2.pack(side=tk.TOP, padx=10, pady=10)  # Place another extra button with purple color

result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="light pink")
result_label.pack(pady=20)  # Place the result label with padding

score_label = tk.Label(root, text="Score: You 0 - Computer 0 - Ties 0", font=("Helvetica", 16), bg="light pink")
score_label.pack(pady=20)  # Place the score label with padding

# Time label
time_label = tk.Label(root, text="", font=("Helvetica", 14), bg="light pink")
time_label.pack(side=tk.TOP, anchor=tk.NE, padx=20, pady=10)  # Place the time label at the top-right corner

# Start the time update function
update_time()  # Call the update_time function to start updating the time

# Start the main event loop
root.mainloop()  # Run the Tkinter event loop to keep the window open
