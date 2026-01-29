import tkinter as tk
import random

def generate():
    start = int(entry_start.get())
    end = int(entry_end.get())
    result = random.randint(start, end)
    label_result.config(text="Random Number: " + str(result))

window = tk.Tk()
window.title("Random Number Generator")
window.geometry("300x200")

tk.Label(window, text="Start Number").pack()
entry_start = tk.Entry(window)
entry_start.pack()

tk.Label(window, text="End Number").pack()
entry_end = tk.Entry(window)
entry_end.pack()

tk.Button(window, text="Generate", command=generate).pack(pady=10)

label_result = tk.Label(window, text="Random Number: ")
label_result.pack()

window.mainloop()
