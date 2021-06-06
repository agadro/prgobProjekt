from tkinter import *
from tkinter import Tk
import base64
import tkinter.font as font

# szyfrowanie i deszyfrowanie metodą Cezara

KLUCZ = 3
key = 'C'


def szyfruj_lub_deszyfruj(input_txt):
    input_txt = input_txt.upper()
    output_txt = []
    for pos in range(0, len(input_txt)):
        letter_row = 'A'
        letter_txt = input_txt[pos]
        while letter_txt != key[pos % len(key)]:
            letter_txt = chr((ord(letter_txt) - ord('A') + 1) % 26
                             + ord('A'))
            letter_row = chr((ord(letter_row) - ord('A') + 1) % 26
                             + ord('A'))
        output_txt.append(letter_row)
    return ''.join(output_txt)


def szyfruj_cezar(txt):
    txt = txt.lower()
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny


def deszyfruj_cezar(tekst):
    odszyfrowany = ""
    KLUCZM = KLUCZ % 26
    for znak in tekst:
        if ord(znak) - KLUCZM < 97:
            odszyfrowany += chr(ord(znak) - KLUCZM + 26)
        else:
            odszyfrowany += chr(ord(znak) - KLUCZM)
    return odszyfrowany


# szyfrowanie i deszyfrowanie metodą Base64

def szyfruj_base64(txt):
    message = txt
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def deszyfruj_base64(txt):
    base64_message = txt
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


# tworzenie okna aplikacji i ustawienie jego domyslnych wymiarow

okno = Tk()
okno.title("Lockify")
okno.geometry("400x500")
okno.iconbitmap(r'favicon.ico')
okno.configure(bg='khaki3')
# okno.background


# tworzenie podzialu

topFrame = Frame(okno)
topFrame.pack()
topFrame.configure(bg='khaki3')

bottomFrame = Frame(okno)
bottomFrame.pack(side=BOTTOM)
bottomFrame.configure(bg='khaki3')
scroll = Scrollbar(okno)
scroll.pack(side= RIGHT, fill=Y)
mylist = Listbox(okno, yscrollcommand = scroll.set, relief=FLAT, bg='khaki1', height=20)
mylist.pack( fill = BOTH )
scroll.config(command = mylist.yview)

# tworzenie okna do wprowadzania danych

wprowadz_tekst = Entry(topFrame, width=100)
wprowadz_tekst.pack(side=BOTTOM)


# deklaracja metod implementujących działanie poszczególnych szyfrów

class Szyfruj:
    def __init__(self):
        self.pozyskany_tekst = ''
        self.pozyskany_tekst2 = ''
        self.pozyskany_tekst3 = ''

    def et_szyfr_cezar(self):
        if not wprowadz_tekst.get():
            mylist.insert(END,"WPISZ TEKST")
        else:
            self.pozyskany_tekst = szyfruj_cezar(wprowadz_tekst.get())
            mylist.insert(END, self.pozyskany_tekst)

    def et_deszyfr_cezar(self):
        if not self.pozyskany_tekst:
            mylist.insert(END, "WPISZ TEKST")
        else:
            mylist.insert(END, deszyfruj_cezar(self.pozyskany_tekst))

    def et_szyfr_base64(self):
        if not wprowadz_tekst.get():
            mylist.insert(END, "WPISZ TEKST")
        else:
            self.pozyskany_tekst2 = szyfruj_base64(wprowadz_tekst.get())
            mylist.insert(END, self.pozyskany_tekst2)

    def et_deszyfr_base64(self):
        if not self.pozyskany_tekst2:
            mylist.insert(END, "WPISZ TEKST")
        else:
            mylist.insert(END, deszyfruj_base64(self.pozyskany_tekst2))

    def et_szyfruj(self):
        if not wprowadz_tekst.get():
            mylist.insert(END, "WPISZ TEKST")
        else:
            self.pozyskany_tekst3 = szyfruj_lub_deszyfruj(wprowadz_tekst.get())
            mylist.insert(END, self.pozyskany_tekst3)

    def et_deszyfruj(self):
        if not self.pozyskany_tekst3:
            mylist.insert(END, "WPISZ TEKST")
        else:
            mylist.insert(END, szyfruj_lub_deszyfruj(self.pozyskany_tekst3))


def usun():
    mylist.delete(END)


myFont = font.Font(family='Verdana')
# tworzenie przyciskow i przypisywanie do nich funkcji

podaj_slowo = Label(topFrame, text='Podaj słowo', relief=FLAT, background='khaki2')

szyfr = Szyfruj()

deleteB = Button(bottomFrame, text='Usuń', command=usun)


przycisk_sz_cezar = Button(bottomFrame, text='Szyfr Cezara', command=szyfr.et_szyfr_cezar,
                           background='khaki4', activebackground='black', activeforeground='khaki4',
                           relief=FLAT
                           )
przycisk_desz_cezar = Button(bottomFrame, text='Deszyfrowanie Cezar', command=szyfr.et_deszyfr_cezar,
                             background='khaki4', activebackground='black', activeforeground='khaki4',
                             relief=FLAT
                             )

przycisk_sz_base64 = Button(bottomFrame, text='Szyfr Base64', command=szyfr.et_szyfr_base64,
                            background='khaki4', activebackground='black', activeforeground='khaki4',
                            relief=FLAT
                            )

przycisk_desz_base64 = Button(bottomFrame, text='Deszyfrowanie Base64', command=szyfr.et_deszyfr_base64,
                              background='khaki4', activebackground='black', activeforeground='khaki4',
                              relief=FLAT
                              )

przycisk_sz_4kw = Button(bottomFrame, text='Szyfr Beauforta', command=szyfr.et_szyfruj,
                         background='khaki4', activebackground='black', activeforeground='khaki4',
                         relief=FLAT
                         )

przycisk_desz_4kw = Button(bottomFrame, text='Deszyfrowanie Beaufort', command=szyfr.et_deszyfruj,
                           background='khaki4', activebackground='black', activeforeground='khaki4',
                           relief=FLAT
                           )
podaj_slowo['font'] = myFont
podaj_slowo.pack(side=TOP)

przycisk_sz_cezar['font'] = myFont
przycisk_desz_cezar['font'] = myFont
przycisk_sz_cezar.grid(row=1, column=1, padx=5, pady=5)
przycisk_desz_cezar.grid(row=1, column=2, padx=5, pady=5)

przycisk_sz_base64['font'] = myFont
przycisk_desz_base64['font'] = myFont
przycisk_sz_base64.grid(row=2, column=1, padx=5, pady=5)
przycisk_desz_base64.grid(row=2, column=2, padx=5, pady=5)

przycisk_sz_4kw['font'] = myFont
przycisk_desz_4kw['font'] = myFont
przycisk_sz_4kw.grid(row=3, column=1, padx=5, pady=5)
przycisk_desz_4kw.grid(row=3, column=2, padx=5, pady=5)

deleteB['font'] = myFont
deleteB.grid(row=4, column=1, padx=5, pady=5)

okno.mainloop()
