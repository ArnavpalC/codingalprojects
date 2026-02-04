import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")
root.resizable(False, False)

rock_img = ImageTk.PhotoImage(Image.open("rock.jpg").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

choices = ["Rock", "Paper", "Scissors"]

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"))
title.pack(pady=10)

user_label = tk.Label(root, text="Your Choice", font=("Arial", 14))
user_label.pack()

user_choice_img = tk.Label(root)
user_choice_img.pack(pady=5)

computer_label = tk.Label(root, text="Computer's Choice", font=("Arial", 14))
computer_label.pack()

computer_choice_img = tk.Label(root)
computer_choice_img.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

def play(user_choice):
    computer_choice = random.choice(choices)

    user_choice_img.config(image=images[user_choice])
    computer_choice_img.config(image=images[computer_choice])

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
    else:
        result = "You Lose 😢"

    result_label.config(text=result)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, image=rock_img, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, image=paper_img, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, image=scissors_img, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
