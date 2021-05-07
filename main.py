
from tkinter import *
from tkinter import messagebox
from tkinter import Tk




KLUCZ = 3


def szyfruj(txt):
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny


"""def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:n")
    print("Ciąg zaszyfrowany:n, szyfruj(tekst))
    return 0"""



okno = Tk()
okno.geometry("300x300")




topFrame = Frame(okno)
topFrame.pack()
bottomFrame = Frame(okno)
bottomFrame.pack(side = BOTTOM)

entry1 = Entry(okno)
entry1.pack(side = TOP)

def labelka():
    mylable = Label(okno, text=szyfruj(entry1.get()))
    mylable.pack()


podaj_slowo = Label(topFrame, text = 'Podaj słowo')


przycisk1 = Button(bottomFrame, text = 'guzik', command = labelka)
przycisk2 = Button(bottomFrame, text = 'test', command = szyfruj('morda'))




podaj_slowo.pack(side = LEFT)

przycisk2.pack(side = LEFT)
przycisk1.pack(side = TOP)





okno.mainloop()


