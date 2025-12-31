import tkinter as tk
from tkinter import messagebox
import random

# --- Encryption Function (Caesar Cipher) ---
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# --- Game Data ---
WORDS = [
    "HELLO WORLD", "PYTHON ROCKS", "SECRET CODE",
    "ENCRYPTION", "CRYPTOGRAPHY", "KEEP IT SAFE", "HACK THE PLANET"
]

# --- Global Variables ---
score = 0
current_word = ""
encrypted_word = ""
current_shift = 0
difficulty = "Easy"  # Default difficulty

# --- Functions ---
def new_round():
    """Start a new round."""
    global current_word, encrypted_word, current_shift
    current_word = random.choice(WORDS)
    current_shift = random.randint(1, 5)  # 👈 Keep shift between 1 and 5
    encrypted_word = caesar_encrypt(current_word, current_shift)

    # Update interface
    label_question.config(text=f"Encrypted: {encrypted_word}")
    entry_guess.delete(0, tk.END)
    label_hint.config(text="Hint: ???")

    # Easy mode shows shift automatically
    if difficulty == "Easy":
        label_hint.config(text=f"Hint: Shift = {current_shift}")

    label_score.config(text=f"Score: {score}")

def check_answer():
    """Check player's answer."""
    global score
    user_guess = entry_guess.get().strip().upper()

    if user_guess == current_word:
        score += 1
        messagebox.showinfo("Correct!", f"✅ Correct! Shift was {current_shift}")
    else:
        score -= 1
        messagebox.showerror("Wrong!", f"❌ Wrong! The correct answer was '{current_word}' (shift={current_shift})")
    new_round()

def give_hint():
    """Reveal the shift value."""
    label_hint.config(text=f"Hint: Shift = {current_shift}")

def set_difficulty(level):
    """Set difficulty level and start new game."""
    global difficulty
    difficulty = level
    messagebox.showinfo("Difficulty", f"Difficulty set to {level}")
    new_round()

# --- GUI SETUP ---
root = tk.Tk()
root.title("🔐 Cryptography Game (Shift ≤ 5)")
root.geometry("520x420")
root.config(bg="#1e1e2f")

# --- Widgets ---
title = tk.Label(root, text="🧠 Cryptography Challenge", font=("Arial", 20, "bold"), fg="cyan", bg="#1e1e2f")
title.pack(pady=10)

label_question = tk.Label(root, text="", font=("Consolas", 16), fg="white", bg="#1e1e2f")
label_question.pack(pady=20)

entry_guess = tk.Entry(root, font=("Consolas", 16), justify="center")
entry_guess.pack(pady=10)

btn_check = tk.Button(root, text="Check Answer", font=("Arial", 14), bg="green", fg="white", command=check_answer)
btn_check.pack(pady=5)

btn_hint = tk.Button(root, text="Give Hint", font=("Arial", 12), bg="orange", fg="black", command=give_hint)
btn_hint.pack(pady=5)

label_hint = tk.Label(root, text="Hint: ???", font=("Arial", 12), fg="yellow", bg="#1e1e2f")
label_hint.pack(pady=5)

label_score = tk.Label(root, text="Score: 0", font=("Arial", 14), fg="white", bg="#1e1e2f")
label_score.pack(pady=10)

# Difficulty buttons
frame_diff = tk.Frame(root, bg="#1e1e2f")
frame_diff.pack(pady=5)
tk.Button(frame_diff, text="Easy", bg="lightgreen", command=lambda: set_difficulty("Easy")).grid(row=0, column=0, padx=10)
tk.Button(frame_diff, text="Hard", bg="red", fg="white", command=lambda: set_difficulty("Hard")).grid(row=0, column=1, padx=10)

btn_new = tk.Button(root, text="New Game", font=("Arial", 12), bg="blue", fg="white", command=new_round)
btn_new.pack(pady=10)

# Start game
new_round()

root.mainloop()
