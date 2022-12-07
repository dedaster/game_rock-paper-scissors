# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 04:00:06 2022

@author: dedaster
"""

import tkinter as tk # импортируем библиотеку
import random

# функция закрытия окна
def close_game(): # функция действия после нажатия кнопки
    window.destroy() # закрытие окна
  
# функция вывода выбора игрока
def rock():
    player_ch = 'Камень'
    player = tk.Label(window, text = player_ch, width = 25, textvariable=rock, height = 5, bg = "white", fg = "black").grid(row = 1, column = 0)
    comp_choice(player_ch)
    
def scissors():
    player_ch = 'Ножницы'
    player = tk.Label(window, text = player_ch, width = 25, height = 5, bg = "white", fg = "black").grid(row = 1, column = 0)
    comp_choice(player_ch)
    
def paper():
    player_ch = 'Бумага'
    player = tk.Label(window, text = player_ch, width = 25, height = 5, bg = "white", fg = "black").grid(row = 1, column = 0)
    comp_choice(player_ch)
    
def comp_choice(player_ch):
    comp_ch = random.choice(['Камень','Ножницы','Бумага'])
    comp = tk.Label(window, text = comp_ch, width = 25, height = 5, bg = "white", fg = "black").grid(row = 1, column = 2)
    l = ["Камень", "Ножницы", "Бумага"]
    win = ["Победа за тобой!", "Поражение", "Ничья"]
    if player_ch == l[0] and comp_ch == l[1]:
        winner = win[0]
    elif player_ch == l[0] and comp_ch == l[2]:
        winner = win[1]
    elif player_ch == l[1] and comp_ch == l[0]:
        winner = win[1]
    elif player_ch == l[1] and comp_ch == l[2]:
        winner = win[0]
    elif player_ch == l[2] and comp_ch == l[0]:
        winner = win[0]
    elif player_ch == l[2] and comp_ch == l[1]:
        winner = win[1]
    else:
        winner = win[2]       
    res = tk.Label(window, text = winner, width = 25, height = 5, bg = "white", fg = "black").grid(row = 0, column = 1)

#внешний вид окна
window = tk.Tk()
window.title("Камень-ножницы-бумага. GOTY Edition")

# меню результатов игры
res = tk.Label(window, text = "Who?", width = 25, height = 5, bg = "white", fg = "black").grid(row = 0, column = 1)
player = tk.Label(window, text = "Твой ход", width = 25, height = 5, bg = "white", fg = "black").grid(row = 1, column = 0)
vs = tk.Label(window, text = "против", width = 25, height = 3, fg = "black").grid(row = 1, column = 1)
comp = tk.Label(window, text = "Ход компьютера", width = 25, height = 5, bg = "white", fg = "black").grid(row = 1, column = 2)
#кнопки выбора
btn_rock = tk.Button(text = "Камень", width = 25, height = 5, bg = "white", fg = "black", command = rock).grid(row = 2, column = 0) # command отсылается к функции, которая выполнится по нажатию кнопки
btn_scissors = tk.Button(text = "Ножницы", width = 25, height = 5, bg = "white", fg = "black", command = scissors).grid(row = 2, column = 1) # command отсылается к функции, которая выполнится по нажатию кнопки
btn_paper = tk.Button(text = "Бумага", width = 25, height = 5, bg = "white", fg = "black", command = paper).grid(row = 2, column = 2) # command отсылается к функции, которая выполнится по нажатию кнопки
# кнопка выхода из игры
button = tk.Button(text = "Выйти из игры", width = 25, height = 3, bg = "white", fg = "black", command = close_game).grid(row = 3, column = 2) # command отсылается к функции, которая выполнится по нажатию кнопки

window.mainloop()