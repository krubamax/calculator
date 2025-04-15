import tkinter as tk

# สร้างหน้าต่าง
window = tk.Tk()
window.title("เครื่องคิดเลข")
window.geometry("400x600")
window.configure(bg="lightblue")

# ช่องกรอกตัวเลข
input_entry = tk.Entry(window, font=("Arial", 18), bg="white", justify="right")
input_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ฟังก์ชันเมื่อกดปุ่มตัวเลข
def insert_number(number):
    input_entry.insert(tk.END, number)

# ฟังก์ชันล้างหน้าจอ
def clear():
    input_entry.delete(0, tk.END)

# ฟังก์ชันคำนวณ
def calculate():
    try:
        result = eval(input_entry.get())  # ใช้ eval เพื่อคำนวณ เช่น "1+2*3"
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, str(result))
    except:
        input_entry.delete(0, tk.END)
        input_entry.insert(tk.END, "Error")

# กำหนดปุ่มตัวเลขและเครื่องหมาย
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

# วนลูปสร้างปุ่มเป็นตาราง 4x4
for r, row in enumerate(buttons):
    for c, button in enumerate(row):
        if button == "C":
            action = clear
        elif button == "=":
            action = calculate
        else:
            action = lambda x=button: insert_number(x)

        tk.Button(window, text=button, font=("Arial", 14), bg="lightgreen", activebackground="lightgreen",
                  width=6, height=2, command=action).grid(row=r+1, column=c, padx=5, pady=5)

# เริ่มทำงาน GUI
window.mainloop()
