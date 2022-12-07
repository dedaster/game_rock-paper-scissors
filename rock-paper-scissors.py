# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 04:00:06 2022

@author: dedaster
"""

import tkinter as tk # импортируем библиотеку
import random

h = 3 # высота кнопок
w = 20 # ширина кнопок

# функция закрытия игры
def close_game():
    window.destroy()
  
# функции выбора игрока
def rock():
    player_ch = 'Камень'
    player = tk.Label(window, text = player_ch, width = w, textvariable=rock, height = h, bg = "white", fg = "black").grid(row = 3, column = 0)
    comp_choice(player_ch)
    
def scissors():
    player_ch = 'Ножницы'
    player = tk.Label(window, text = player_ch, width = w, height = h, bg = "white", fg = "black").grid(row = 3, column = 0)
    comp_choice(player_ch)
    
def paper():
    player_ch = 'Бумага'
    player = tk.Label(window, text = player_ch, width = w, height = h, bg = "white", fg = "black").grid(row = 3, column = 0)
    comp_choice(player_ch)
    
# функция случайного выбора компьютера и итога игры
def comp_choice(player_ch):
    comp_ch = random.choice(['Камень','Ножницы','Бумага'])
    tk.Label(window, text = comp_ch, width = w, height = h, bg = "white",).grid(row = 3, column = 2)
    opt = ["Камень", "Ножницы", "Бумага"]
    win = ["Победа за тобой!", "Поражение", "Ничья"]
    # условия результатов
    if player_ch == opt[0] and comp_ch == opt[1]:
        winner = win[0]
    elif player_ch == opt[0] and comp_ch == opt[2]:
        winner = win[1]
    elif player_ch == opt[1] and comp_ch == opt[0]:
        winner = win[1]
    elif player_ch == opt[1] and comp_ch == opt[2]:
        winner = win[0]
    elif player_ch == opt[2] and comp_ch == opt[0]:
        winner = win[0]
    elif player_ch == opt[2] and comp_ch == opt[1]:
        winner = win[1]
    else:
        winner = win[2]
        
    # списки комментариев к результатам
    reswin = random.choice(["Так держать!", "Ты потрясающий!", "Невероятный манёвр!"])
    reslose = random.choice(["Повезёт в другой раз!", "Всё ещё впереди!", "У тебя получится!"])
    resdraw = random.choice(["Вот это схватка!", "Встретились 2 титана!", "Какое напряжение!"])
    # вывод результата
    if winner == win[0]:
        res = tk.Label(window, text = winner, width = w*3, height = h, bg = "white", fg = "green").grid(row = 0, columnspan = 3)
        comments = tk.Label(window, text = reswin, width = w, height = 1).grid(row = 1, column = 1, pady = 5)
    elif winner == win[1]:
        res = tk.Label(window, text = winner, width = w*3, height = h, bg = "white", fg = "red").grid(row = 0, columnspan = 3)
        comments = tk.Label(window, text = reslose, width = w, height = 1).grid(row = 1, column = 1, pady = 5)
    else:
        res = tk.Label(window, text = winner, width = w*3, height = h, bg = "white", fg = "black").grid(row = 0, columnspan = 3)
        comments = tk.Label(window, text = resdraw, width = w, height = 1).grid(row = 1, column = 1, pady = 5)
            
        
#внешний вид окна
window = tk.Tk()
window.title("Камень-ножницы-бумага. GOTY Edition")
# подписи игроков
tk.Label(window, text = "Твой ход:", width = w, height = 1, fg = "black").grid(row = 2, column = 0)
tk.Label(window, width = w, height = 1, fg = "black").grid(row = 2, column = 1)
tk.Label(window, text = "Ход компьютера:", width = w, height = 1, fg = "black").grid(row = 2, column = 2)
# меню результатов игры
res = tk.Label(window, text = "Кто победит?", width = w*3, height = h, bg = "white", fg = "black").grid(row = 0, columnspan = 3)
comments = tk.Label(window, text = "Что же ждёт нас сегодня?", width = w, height = 1).grid(row = 1, column = 1, pady = 5)
player = tk.Label(window, width = w, height = h, bg = "white", fg = "black").grid(row = 3, column = 0)
vs = tk.Label(window, text = "против", width = w, height = h, bg = "white", fg = "black").grid(row = 3, column = 1)
comp = tk.Label(window, width = w, height = h, bg = "white", fg = "black").grid(row = 3, column = 2)
#кнопки выбора
btn_rock = tk.Button(text = "Камень", width = w, height = h, bg = "white", fg = "black", command = rock).grid(row = 4, column = 0, pady = 5)
btn_scissors = tk.Button(text = "Ножницы", width = w, height = h, bg = "white", fg = "black", command = scissors).grid(row = 4, column = 1)
btn_paper = tk.Button(text = "Бумага", width = w, height = h, bg = "white", fg = "black", command = paper).grid(row = 4, column = 2)
# кнопка выхода из игры
button = tk.Button(text = "Выйти из игры", width = w, height = 1, bg = "white", fg = "black", command = close_game).grid(row = 5, column = 2, pady = 5)

window.mainloop()