from tkinter import *  #kerakli narsalarni import qilish
import pandas  #kerakli narsalarni import qilish
import random  #kerakli narsalarni import qilish

try:  #harakat qilib ko'r
    data = pandas.read_csv("data/words_to_learn.csv")  # csvni o'qi
except FileNotFoundError:  #bu hato bo'lsa
    data_french = pandas.read_csv("data/french_words.csv")  #bu csvni o'qi
    words_list = pandas.DataFrame.to_dict(data_french,
                                          orient="records")  #uni [{}] mana bu shaklga keltir https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html men buni shu yerdan o'rgandim
else:  #hech biri b'lmasa
    words_list = pandas.DataFrame.to_dict(data, orient="records")  #uni [{}] mana bu shaklga keltir

random_word = {}  #dictionary yarat

print(words_list)


def time_next():  #funksiya yarat bu funksiya ekranni vaqtida almashtirsin va french so'zi orqasiga esa oq qo'yib qo'ysin
    global random_word  #randomni Butun faylga qo'shish
    global timer
    random_word = random.choice(words_list)  #random wordga so'z qo'sh
    timer = window.after(5000,
                         changebgcolor)  #pastagi timerni qayta qilish sababi biz uni funksiyani ichida ishlatamiz
    window.after_cancel(
        timer)  #men buni shu yerdan o;rgandim https://stackoverflow.com/questions/25702094/tkinter-after-cancel-in-python
    canvas.itemconfig(canvas_image, image=bg_front)  #rasm qo'yish
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random_word["French"])  #random wordni wo'yish


def changebgcolor():  #yani almashtirish so'z va backgroundni
    canvas.itemconfig(canvas_image, image=bg_back)  #tepadagi bilan bir hul
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=random_word["English"])


def knowperson():  #agarda inson o'rgangan bo'sa
    words_list.remove(random_word)  # bu so'zni o'chir
    time_next()  #funksiyani ishlat yani yana french so'z ber
    data = pandas.DataFrame(words_list)  # qavslarni olib tasha
    data.to_csv("data/words_to_learn.csv", index=False)  #csvf=ga o'gir


window = Tk()
window.title("French Flash Cards")
window.config(bg="#B2DDC5")

canvas = Canvas(height=326, width=400, bg="#B2DDC5", highlightthickness=0)

bg_front = PhotoImage(file="images/card_front.png")
bg_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(305, 163, image=bg_front)

canvas.grid(row=0, column=0, columnspan=2, pady=30, padx=50)
title = canvas.create_text(200, 120, font=("arial", 25, "italic"), text="French")

word = canvas.create_text(200, 180, font=("arial", 45, "bold"), text="Trouve")

check_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_button_image, highlightthickness=0, command=knowperson)
right_button.grid(row=1, column=1, pady=30)

x_button_image = PhotoImage(file="images/wrong.png")
left_button = Button(image=x_button_image, highlightthickness=0, command=time_next)
left_button.grid(row=1, column=0)

timer = window.after(5000,
                     changebgcolor)  # men buni ochganimni sababi funksiyanoi ichida funksiya ishlatilsa hato bo'ladi
time_next()

window.mainloop()
