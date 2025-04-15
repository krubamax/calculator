import random
import tkinter as tk

windows = tk.Tk()
windows.title("สุ่มหนัง")
windows.geometry("400x300")
windows.configure(bg="lightblue")

title_lable = tk.Label(windows, text="ดูหนังไรดีง่ะะ", font=("Arial", 16))
title_lable.pack(pady=10)

name_move = [
    # หนังไทย (Thai Movies)
    "Bang Rajan", "Tears of the Black Tiger", "The Iron Ladies", "Mysterious Object at Noon",
    "Shutter", "Ong-Bak: The Thai Warrior", "Pee Mak", "The Medium", "One for the Road", "Ghost Lab",
    "Deep", "Classic Again", "Low Season", "Pee Nak 2", "The Maid", "Thibaan × BNK48", "Who",
    "Mother Gamer", "The Con-Heartist", "Long Live Love!", "Not Friends", "When a Snail Falls in Love",
    "Love You to Debt", "How to Make Millions Before Grandma Dies", "Hunger", "404 Run Run",
    "Frozen Hot Boys", "Death Whisperer", "The Pool", "Bad Genius", "The Promise", "Brother of the Year",
    "Friend Zone", "Happy Old Year", "The Whole Truth", "The Girl from Nowhere", "The Forest",
    "The Blue Hour", "By the Time It Gets Dark", "Pop Aye", "The Island Funeral", "The Road to Mandalay",
    "The Teacher's Diary", "I Fine..Thank You..Love You", "ATM: Er Rak Error", "Hello Stranger",
    "Crazy Little Thing Called Love", "The Love of Siam", "Fan Chan", "Syndromes and a Century",

    # หนังยุโรป (European Movies)
    "The Last Emperor", "The Pianist", "Life Is Beautiful", "The King's Speech", "Léon: The Professional",
    "Amélie", "Cinema Paradiso", "The Lives of Others", "Pan's Labyrinth", "The Intouchables",
    "The Hunt", "Blue Is the Warmest Colour", "The Great Beauty", "Ida", "Son of Saul", "Cold War",
    "Portrait of a Lady on Fire", "Another Round", "The Worst Person in the World", "Triangle of Sadness",
    "Close", "La Haine", "Run Lola Run", "The White Ribbon", "Melancholia", "The Lobster", "The Square",
    "The Favourite", "Parasite", "The Father", "Quo Vadis, Aida?", "Flee", "Benedetta", "The Hand of God",
    "Compartment No. 6", "The Eight Mountains", "EO", "Saint Omer", "Corsage", "Alcarràs", "Aftersun",
    "Rye Lane", "La Chimera", "Perfect Days", "The Zone of Interest", "Anatomy of a Fall",
    "The Taste of Things", "The Teachers' Lounge", "Fallen Leaves"
]

move_list = tk.Label(windows, text="", font=("Arial", 16), bg="lightblue")
move_list.pack(pady=10)

btn_sum = tk.Button(
    windows, text="สุ่มหนัง", font=("Arial", 14),
    command=lambda: move_list.configure(text=random.choice(name_move)), bg="lightgreen", activebackground="lightgreen"
)
btn_sum.pack(pady=10)

windows.mainloop()
