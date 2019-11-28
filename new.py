from Tkinter import *
import ttk

window = Tk()
window.title("MA HOA")
#Tieu de
titleLabel = Label(window, text="MA HOA", font="Arial")
titleLabel.grid(column=0, row=0)
#O nhap van ban
input1Label = Label(window, text="Nhap van ban")
input1Label.grid(column=0, row=1)
input1 = Entry(window, width=40)
input1.grid(column=1, row=1)
#Key
input2Label = Label(window, text="m")
input2Label.grid(column=3, row=1)
input2 = Entry(window, width=10)
input2.grid(column=4, row=1)
input3Label = Label(window, text="k")
input3Label.grid(column=5, row=1)
input3 = Entry(window, width=10)
input3.grid(column=6, row=1)
#O xuat du lieu da ma hoa
output1Label = Label(window, text="Ma hoa")
output1Label.grid(column=0, row=2)
output1 = Entry(window, width=40)
output1.grid(column=1, row=2)
#O xuat du lieu da giai ma
output2Label = Label(window, text="Giai ma")
output2Label.grid(column=0, row=3)
output2 = Entry(window, width=40)
output2.grid(column=1, row=3)


#Chuyen chu thanh so
def char2num(c):
    return ord(c.upper()) - 65


#Chuyen so thanh chu
def num2char(n):
    return chr(n + 65)


#Tim UCLN
def findGCD(b, a):
    tmp = a
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 += tmp
    return x0


#Ma hoa
def encrypt(str, a, b, m):
    r = ""
    for i in str:
        e = (a * char2num(i) + b) % m
        r += num2char(e)
    return r


#Giai ma
def decrypt(str, a, b, m):
    r = ""
    a1 = findGCD(a, m)
    for i in str:
        e = (a1 * (char2num(i) - b)) % m
        r += num2char(e)
    return r


#Bat su kien ma hoa
def clicked_encrypt():
    a, b, m = int(input2.get()), int(input3.get()), 26
    enStr = encrypt(input1.get(), a, b, m)
    output1.delete(0, END)
    output1.insert(INSERT, enStr)


#Bat su kien giai ma
def clicked_decrypt():
    a, b, m = int(input2.get()), int(input3.get()), 26
    deStr = decrypt(output1.get(), a, b, m)
    output2.delete(0, END)
    output2.insert(INSERT, deStr)


#Tao nut nhan ma hoa va giai ma
encryptButton = Button(window, text="Ma hoa", command=clicked_encrypt)
encryptButton.grid(column=7, row=1)
decryptButton = Button(window, text="Giai ma", command=clicked_decrypt)
decryptButton.grid(column=7, row=2)
window.geometry("550x120")
window.mainloop()