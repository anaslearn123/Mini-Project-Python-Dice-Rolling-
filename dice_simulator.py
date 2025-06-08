import tkinter as tk
from tkinter import messagebox
import random

# Dice faces as Unicode characters 🎲
dice_faces = {
    1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
}

# Function to roll the dice
def roll_dice():
    try:
        # Get the number of dice from the entry
        num_dice = int(entry.get())
        
        # Validate input (1 to 10 dice only)
        if num_dice < 1 or num_dice > 10:
            messagebox.showerror("Invalid Input", "Please enter a number between 1 and 10.")
            return
        
        # Generate random numbers between 1 and 6 for each die
        results = [random.randint(1, 6) for _ in range(num_dice)]
        
        # Display dice face results
        result_str = " ".join(dice_faces[result] for result in results)
        result_label.config(text=result_str)
        
        # Show numeric result
        numeric_results = ", ".join(str(result) for result in results)
        numeric_label.config(text=f"Results: {numeric_results}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("🎲 Dice Rolling Simulator")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Dice Rolling Simulator", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Number of Dice Entry Label
entry_label = tk.Label(root, text="Enter number of dice (1-10):", font=("Arial", 12), bg="#f0f0f0")
entry_label.pack()

# Entry Box for Number of Dice
entry = tk.Entry(root, width=5, font=("Arial", 12))
entry.pack(pady=5)

# Roll Button
roll_button = tk.Button(root, text="Roll Dice 🎲", command=roll_dice, bg="green", fg="white", font=("Arial", 12, "bold"))
roll_button.pack(pady=10)

# Result Label (Shows Dice Faces)
result_label = tk.Label(root, text="", font=("Arial", 24), bg="#f0f0f0")
result_label.pack(pady=5)

# Numeric Result Label (Shows Numbers)
numeric_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
numeric_label.pack(pady=5)

# Run GUI
root.mainloop()
