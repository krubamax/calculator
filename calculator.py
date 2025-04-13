import tkinter as tk

#ฟังก์ชันสำหรับการคำนวณสูตรคูณ
def output_text():
    number = int(number_input.get())

    output = ""

    for i in range(1, 13):
        output += f"{number} x {i} = {number * i}\n"

    if output == "":
        output = "กรุณาใส่ตัวเลข"
    elif number < 1 or number > 12:
        output = "กรุณาใส่ตัวเลข 1-12"
    output_number.configure(text=output)# อัพเดตข้อความใน label

window = tk.Tk()
window.title("สูตรคูณ")
window.geometry("400x600")
window.configure(bg="lightblue")

title_label = tk.Label(window, text="สูตรคูณ", font=("Arial", 16), bg="lightblue")
title_label.pack(pady=10)

number_input = tk.Entry(window, font=("Arial", 14), bg="white")
number_input.pack(pady=10)

go_button = tk.Button(
    window, text="ไป", font=("Arial", 14),
    command=output_text, bg="lightgreen", activebackground="lightgreen"
    )
go_button.pack(pady=10)

output_number = tk.Label(window, text="", font=("Arial", 16), bg="lightblue")
output_number.pack(pady=10)

window.mainloop()

#คนเจน X บูรี่เด็กซ์ เจน Z 
