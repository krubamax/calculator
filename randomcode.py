import tkinter as tk

def generate_code():
    text = text_input.get()
    title.configure(text=text)
    text_input.delete(0, tk.END)

window = tk.Tk()
window.title("Random Code Generator")
window.geometry("400x300")

title_lable = tk.Label(window, text="ถืกซะ", font=("Arial", 16))
title_lable.pack(pady=10)

text_input = tk.Entry(window, font=("Arial", 14))
text_input.pack(pady=10)

button = tk.Button(window, text="Generate", font=("Arial", 14), command=generate_code)
button.pack(pady=10)

title = tk.Label(window, text="Random Code", font=("Arial", 16))
title.pack(pady=10)

window.mainloop()
