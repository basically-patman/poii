
from tkinter import *




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

def printowanie_teksta():
    print('Gumis to fajny mis!')



topFrame = Frame(okno)
topFrame.pack()
bottomFrame = Frame(okno)
bottomFrame.pack(side = BOTTOM)

slowo = ''
etykieta = Label(topFrame, text = 'Podaj słowo')
entry1 = Entry(okno, textvariable = slowo)

przycisk1 = Button(bottomFrame, text = 'guzik', command = szyfruj(slowo))

przycisk3 = Button(bottomFrame, text = slowo)
etykieta2 = Label(topFrame, textvariable = slowo)
etykieta.pack(side = LEFT)
entry1.pack(side = TOP)
etykieta2.pack(side = BOTTOM)
przycisk1.pack(side = TOP)
przycisk3.pack(side = BOTTOM)


okno.mainloop()


