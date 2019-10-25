# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
window = Tk()
window.title("Welcome to Demo An Toan Bao Mat Thong Tin")
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ AFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLANT TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)
lb5 = Label(window, text="CIPHER TEXT",font=("Arial", 14))
lb5.grid(column=0, row=4)
ciphertxt3 = Entry(window,width=20)
ciphertxt3.grid(column=1, row=4)
denctxt3 = Entry(window,width=20)
denctxt3.grid(column=3, row=4)
def Char2Num(c): 
    return ord(c.upper())-65
def Num2Char(n): 
    return chr(n+65)

def xgcd(b,a):
    tmp=a
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a!=0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0<0:x0=tmp+x0
    return x0

def encryptAF(txt,a,b,m):
    r=""
    for c in txt:
        e=(a*Char2Num(c)+b )%m
        r=r+Num2Char(e)
    return r

def decryptAF(txt,a,b,m):
    r=""
    a1=xgcd(a,m)
    for c in txt:
        e=(a1*(Char2Num(c)-b ))%m
        r=r+Num2Char(e)
    return r

def clicked():
    a,b,m=int(KEYA1.get()),int(KEYB1.get()),26
    entxt=encryptAF(plaintxt.get(),a,b,m)
    ciphertxt3.delete(0,END)
    #a=int(KEYA1.get())
    ciphertxt3.insert(INSERT,entxt)

def giaima():
    a,b,m=int(KEYA1.get()),int(KEYB1.get()),26
    detxt=decryptAF(ciphertxt3.get(),a,b,m)
    denctxt3.delete(0,END)
    #a=int(KEYA1.get())
    denctxt3.insert(INSERT,detxt)
AFbtn = Button(window, text="Encrypt", command=clicked)
AFbtn.grid(column=5, row=3)
DEAFbtn = Button(window, text="Decrypt", command=giaima)
DEAFbtn.grid(column=2, row=4)
window.geometry('800x200')
window.mainloop()
