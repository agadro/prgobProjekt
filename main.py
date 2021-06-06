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
okno.geometry("400x400")
okno.iconbitmap(r'favicon.ico')
okno.configure(bg='black')
# okno.background


# tworzenie podzialu

topFrame = Frame(okno)
topFrame.pack()
topFrame.configure(bg='blue')
bottomFrame = Frame(okno)
bottomFrame.pack(side=BOTTOM)
bottomFrame.configure(bg='black')

# tworzenie okna do wprowadzania danych

wprowadz_tekst = Entry(okno, width=100)
wprowadz_tekst.pack(side=TOP)


# deklaracja metod implementujących działanie poszczególnych szyfrów

class Szyfruj:
    def __init__(self):
        self.pozyskany_tekst = ''
        self.pozyskany_tekst2 = ''
        self.pozyskany_tekst3 = ''

    def et_szyfr_cezar(self):
        if not wprowadz_tekst.get():
            et_szyfrowanie = Label(okno, text='WPISZ TEKST')
            et_szyfrowanie.pack()
        else:
            et_szyfrowanie = Label(okno, text=szyfruj_cezar(wprowadz_tekst.get()))
            self.pozyskany_tekst = szyfruj_cezar(wprowadz_tekst.get())
            et_szyfrowanie.pack()

    def et_deszyfr_cezar(self):
        if not self.pozyskany_tekst:
            et_szyfrowanie = Label(okno, text='WPISZ TEKST')
            et_szyfrowanie.pack()
        else:
            et_szyfrowanie = Label(okno, text=deszyfruj_cezar(self.pozyskany_tekst))
            et_szyfrowanie.pack()

    def et_szyfr_base64(self):
        if not wprowadz_tekst.get():
            et_szyfrowanie = Label(okno, text='WPISZ TEKST')
            et_szyfrowanie.pack()
        else:
            et_szyfrowanie = Label(okno, text=szyfruj_base64(wprowadz_tekst.get()))
            self.pozyskany_tekst2 = szyfruj_base64(wprowadz_tekst.get())
            et_szyfrowanie.pack()

    def et_deszyfr_base64(self):
        if not self.pozyskany_tekst:
            et_szyfrowanie = Label(okno, text='WPISZ TEKST')
            et_szyfrowanie.pack()
        else:
            et_szyfrowanie = Label(okno, text=deszyfruj_base64(self.pozyskany_tekst2))
            et_szyfrowanie.pack()

    def et_szyfruj(self):
        if not wprowadz_tekst.get():
            et_szyfrowanie = Label(okno, text='WPISZ TEKST')
            et_szyfrowanie.pack()
        else:
            et_szyfrowanie = Label(okno, text=szyfruj_lub_deszyfruj(wprowadz_tekst.get()))
            self.pozyskany_tekst3 = szyfruj_lub_deszyfruj(wprowadz_tekst.get())
            et_szyfrowanie.pack()

    def et_deszyfruj(self):
        if not self.pozyskany_tekst:
            et_szyfrowanie = Label(okno, text='WPISZ TEKST')
            et_szyfrowanie.pack()
        else:
            et_szyfrowanie = Label(okno, text=szyfruj_lub_deszyfruj(self.pozyskany_tekst3))
            et_szyfrowanie.pack()


myFont = font.Font(family='Verdana')
# tworzenie przyciskow i przypisywanie do nich funkcji

podaj_slowo = Label(topFrame, text='Podaj słowo', relief=RIDGE, background='yellow')

szyfr = Szyfruj()
przycisk_sz_cezar = Button(bottomFrame, text='Szyfr Cezara', command=szyfr.et_szyfr_cezar,
                           background='yellow', activebackground='black', activeforeground='yellow',
                           relief=FLAT
                           )
przycisk_desz_cezar = Button(bottomFrame, text='Deszyfrowanie Cezar', command=szyfr.et_deszyfr_cezar,
                             background='yellow', activebackground='black', activeforeground='yellow',
                             relief=FLAT
                             )

przycisk_sz_base64 = Button(bottomFrame, text='Szyfr Base64', command=szyfr.et_szyfr_base64,
                            background='yellow', activebackground='black', activeforeground='yellow',
                            relief=FLAT
                            )

przycisk_desz_base64 = Button(bottomFrame, text='Deszyfrowanie Base64', command=szyfr.et_deszyfr_base64,
                              background='yellow', activebackground='black', activeforeground='yellow',
                              relief=FLAT
                              )

przycisk_sz_4kw = Button(bottomFrame, text='Szyfr Beauforta', command=szyfr.et_szyfruj,
                         background='yellow', activebackground='black', activeforeground='yellow',
                         relief=FLAT
                         )

przycisk_desz_4kw = Button(bottomFrame, text='Deszyfrowanie Beauforta', command=szyfr.et_deszyfruj,
                           background='yellow', activebackground='black', activeforeground='yellow',
                           relief=FLAT
                           )

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

okno.mainloop()
