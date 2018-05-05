# coding: utf-8
# Author: Yosiyoshi
import numpy as np
import random
import tkinter as tk

m= np.matrix([[0, 0, 0, 0], [0, 1, -1, 0], [0, -1, 1, 0], [0, 0, 0, 0]])

#Play automatically for 3 turns as default
t = 0
while t <= 2:
    w = random.randint(0, 2)
    h = random.randint(0, 2)
    while h <= 1:
        if m[w-1, h] + m[w, h] == 0:
            if m[w, h] == 0:
                m[w, h] = 1
                w = w + 1
                if 1 <= w <=2:
                    if m[w-1, h] == m[w+1, h]:
                        m[w-1, h] = 1
                        m[w+1, h] = 1
                elif w <= 1:
                    if m[w, h] == m[w+2, h]:
                        m[w+1, h] = 1
                        m[w+2, h] = 1
                elif w >= 2:
                    if m[w, h] == m[w-2, h]:
                        m[w-1, h] = 1
                        m[w-1, h] = 1
            elif m[w, h] == 1:
                m[w+1, h] = 1
                m[w+2, h] = 1
                w = w + 1
        elif m[w, h] + m[w, h+1] == 0:
            if m[w, h] == 0:
                w = w + 1
            elif m[w, h] == 1:
                if w <= 1:
                    m[w, h+1] = 1
                    m[w, h+2] = 1
                w = w + 1
        elif m[w, h] + m[w+1, h+1] == 0:
            if m[w, h] == 0:
                w = w + 1
            elif m[w, h] == 1:
                if w <= 1:
                    m[w+1, h+1] = 1
                    m[w+2, h+2] = 1
                w = w + 1
        h = h + 1
        a = 0
        while a <= 3:
            if m[a, 0] == 1:
                if m[a, 2] == 1:
                    m[a, 1] = 1
            elif m[a, 1] == 1:
                if m[a, 3] == 1:
                    m[a, 2] = 1
            a = a + 1
    w = random.randint(0, 2)
    h = random.randint(0, 2)
    while h <= 1:
        if m[w-1, h] + m[w, h] == 0:
            if m[w, h] == 0:
                m[w, h] = -1
                w = w + 1
                if 1 <= w <=2:
                    if m[w-1, h] == m[w+1, h]:
                        m[w-1, h] = -1
                        m[w+1, h] = -1
                elif w == 1:
                    if m[w, h] == m[w+2, h]:
                        m[w+1, h] = -1
                        m[w+2, h] = -1
                elif w >= 2:
                    if m[w, h] == m[w-2, h]:
                        m[w-1, h] = -1
                        m[w-1, h] = -1
            elif m[w, h] == -1:
                if 0 <= w <= 1:
                    m[w+1, h] = -1
                    m[w+2, h] = -1
                w = w + 1
        elif m[w, h] + m[w, h+1] == 0:
            if m[w, h] == 0:
                w = w + 1
            elif m[w, h] == -1:
                if w <= 1:
                    m[w, h+1] = -1
                    m[w, h+2] = -1
                w = w + 1
        elif w <= 2:
            if m[w, h] + m[w+1, h+1] == 0:
                if m[w, h] == 0:
                    w = w + 1
                elif m[w, h] == -1:
                    if w <= 1:
                        m[w+1, h+1] = -1
                        m[w+2, h+2] = -1
                    w = w + 1
        h = h + 1
        a = 0
        while a < 3:
            if m[a, 0] == -1:
                if m[a, 2] == -1:
                    m[a, 1] = -1
            elif m[a, 1] == -1:
                if m[a, 3] == -1:
                    m[a, 2] = -1
            a = a + 1
    t = t + 1
root = tk.Tk()
root.title('result')
Static = tk.Label(text=m)
Static.pack()
root.mainloop()
