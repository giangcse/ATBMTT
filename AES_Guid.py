# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
from Crypto.Cipher import AES
from Crypto import Random

window = Tk()
window.title("MÃ HÓA AES")
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="MÃ HÓA AES",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
plainlb3 = Label(window, text="PLANT TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYB1 = Entry(window,width=20)
KEYB1.grid(column=3, row=3)
lb5 = Label(window, text="CIPHER TEXT",font=("Arial", 14))
lb5.grid(column=0, row=4)
ciphertxt3 = Entry(window,width=20)
ciphertxt3.grid(column=1, row=4)
denctxt3 = Entry(window,width=20)
denctxt3.grid(column=3, row=4)

def mahoa():
    plaintext = plaintxt.get()
    key = KEYB1.get()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(plaintext)
    ciphertxt3.delete(0, END)
    ciphertxt3.insert(INSERT, msg)

def giaima():
    encrypttext = ciphertxt3.get()
    key = KEYB1.get()
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = cipher.decrypt(encrypttext)
    denctxt3.delete(0, END)
    denctxt3.insert(INSERT, msg)
AFbtn = Button(window, text="MÃ HÓA", command=mahoa)
AFbtn.grid(column=5, row=3)
DEAFbtn = Button(window, text="GIẢI MÃ", command=giaima)
DEAFbtn.grid(column=5, row=4)
window.geometry('600x200')
window.mainloop()
