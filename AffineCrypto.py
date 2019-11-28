#Giai thuat Eclid mo rong
def extendedEclidean(b, a):
    temp = a
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = b // a, a, b % a
        x0, x1 = x1, x0 - x1 * q
        y0, y1 = y1, y0 - y1 * q
    if x0 < 0: x0 += temp
    return x0


#Chuyen chu thanh so
def char2num(c):
    return ord(c.upper()) - 65


#Chuyen so thanh chu
def num2char(n):
    return chr(n + 65)


#Ma hoa
def encrypt(str, a, b):
    r = ""
    for i in str:
        e = (a * char2num(i) + b) % 26
        r += num2char(e)
    return r


#Giai ma
def decrypt(str, a, b):
    r = ""
    a1 = extendedEclidean(a, 26)
    for i in str:
        e = (a1 * (char2num(i) - b)) % 26
        r += num2char(e)
    return r


if __name__ == "__main__":
    str = raw_input("Nhap chuoi: ")
    enStr = ""
    a, b = int(input("Nhap a: ")), int(input("Nhap b: "))
    enStr += encrypt(str, a, b)
    print("Chuoi da ma hoa: " + enStr)
    print("Chuoi da giai ma: " + decrypt(enStr, a, b))
    pass
