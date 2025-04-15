# import requests
# import tkinter as tk
# url = "https://api.open-meteo.com/v1/forecast?latitude=14.904&longitude=105.047&current_weather=true"

# def show_weather():
#     response = requests.get(url)
#     data = response.json()
#     temperature = data["current_weather"]["temperature"]
#     water_label.config(text=f"อุณหภูมิ (เดช): {temperature} °C")

# response = requests.get(url)
# data = response.json()

# print("อุณหภูมิ (เดช):", data["current_weather"]["temperature"], "°C")

# windows = tk.Tk()
# windows.title("อุณหภูมิ")
# windows.geometry("400x300")
# windows.configure(bg="lightblue")

# water_label = tk.Label(windows, text="อุณหภูมิ (เดช)", font=("Arial", 16),command=show_weather)
# water_label.pack(pady=10)



# windows.mainloop()


import requests
import tkinter as tk


url = "https://api.open-meteo.com/v1/forecast?latitude=14.904&longitude=105.047&current_weather=true"

# ฟังก์ชันดึงข้อมูลจาก API แล้วแสดงบน Label
def show_weather():
    response = requests.get(url)
    data = response.json()
    temperature = data["current_weather"]["temperature"]
    water_label1.config(text=f"อุณหภูมิ (เดช): {temperature} °C")


windows = tk.Tk()
windows.title("อุณหภูมิ")
windows.geometry("400x300")
windows.configure(bg="lightblue")


water_label = tk.Label(windows, text="อุณหภูมิ (เดช)", font=("Arial", 16), bg="lightblue")
water_label.pack(pady=10)


water_label1 = tk.Label(windows, text="", font=("Arial", 16), bg="lightblue")
water_label1.pack(pady=10)


btn_check = tk.Button(windows, text="ดูอุณหภูมิ", font=("Arial", 14), command=show_weather, bg="lightgreen")
btn_check.pack(pady=20)

# เริ่มทำงานหน้าต่าง
windows.mainloop()
