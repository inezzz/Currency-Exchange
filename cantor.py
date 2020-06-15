from data_service import DataService
from PIL import ImageTk as tktk
from PIL import Image as immmg
from tkinter import *
import os

class CantorUI:
    def __init__(self, master):
        self.master=master
        color="#c2efc2"
        tytul_kantor = "Kantor Inez"
        master.title(tytul_kantor)
        master.geometry('450x500+100+100')
        master.configure(background=color)
        self.api_url="https://api.nbp.pl/api/exchangerates/tables/A/"
        tablica=DataService(self.api_url).get_data_from_nbp()
        self.set_photo()
        self.set_drop_list_for_first(tablica)
        self.set_drop_list_for_second(tablica)
        self.field_to_entry_quantity_of_currency()
        self.entry_field()
        self.button_to_quit()
        self.button_to_calculate()
        self.make_a_dictionary_of_currency_and_values()
        self.make_a_dictionary_of_currency_and_code()
        self.field_to_displaying_the_result()

    def set_photo(self):
        photo_cantor=tktk.PhotoImage(immmg.open(os.path.join(os.getcwd(),"KANTOR.jpg")))
        photo=Label(self.master, image=photo_cantor)
        photo.pack(side = TOP, fill = BOTH)
        photo.image = photo_cantor

    def set_drop_list_for_first(self, tablica):
        first_change_currency = Label(self.master, text="Wybierz walutę źródłową:", bg="#c2efc2")
        first_change_currency.config(font=("Olympic", 12))
        first_change_currency.place(x=20, y=200)
        self.first_currency = StringVar(self.master)
        self.first_currency.set("Wybierz z listy")
        drop = OptionMenu(self.master, self.first_currency, *tablica, "PLN")
        drop.config(font=("Olympic", 10))
        drop.config(bg="#86df86")
        drop.place(x=250, y=200)

    def set_drop_list_for_second(self, tablica):
        second_change_currency = Label(self.master, text="Wybierz walutę wyjściową:", bg="#c2efc2")
        second_change_currency.config(font=("Olympic", 12))
        second_change_currency.place(x=20, y=250)
        self.second_currency = StringVar(self.master)
        self.second_currency.set("Wybierz z listy")
        dropp = OptionMenu(self.master, self.second_currency, *tablica, "PLN")
        dropp.config(font=("Olympic", 10))
        dropp.config(bg="#86df86")
        dropp.place(x=250, y=250)

    def field_to_entry_quantity_of_currency(self):
        quantity_of_currency=Label(self.master, text="Wprowadź kwotę: ", bg="#c2efc2")
        quantity_of_currency.config(font=("Olympic", 12))
        quantity_of_currency.place(x=20, y=300)

    def entry_field(self):
        self.ilosc=Entry(self.master, justify='center')
        self.ilosc.place(x=160, y=305)

    def quit(self):
        self.master.destroy()

    def button_to_quit(self):
        button=Button(self.master, text='Koniec', width=8, height=1, command=self.quit)
        button.config(font=("Nocturne", 15), bg='#ff8080')
        button.pack(side=BOTTOM, fill=BOTH)

    def button_to_calculate(self):
        button=Button(self.master, text='Oblicz', width=8, height=1, command=self.change_currency)
        button.config(font=("Impact", 15), bg="#5ed45e")
        button.place(x=300, y=300)

    def make_a_dictionary_of_currency_and_values(self):
        currency=DataService(self.api_url).get_data_from_nbp()
        values=DataService(self.api_url).get_currency_values_from_nbp()
        self.dict_currency_and_values = dict(zip(currency, values))

    def make_a_dictionary_of_currency_and_code(self):
        currency=DataService(self.api_url).get_data_from_nbp()
        code=DataService(self.api_url).get_code_currency_from_nbp()
        self.dict_currency_and_code = dict(zip(currency, code))

    def change_currency(self):
        first_currency=self.first_currency.get()
        second_currency=self.second_currency.get()
        ilosc=float(self.ilosc.get())
        if first_currency == 'PLN':
            wynik1=ilosc/self.dict_currency_and_values[second_currency]
            tekst1=str(round(wynik1, 2)) + " " + self.dict_currency_and_code[second_currency]
            self.finish_result.config(text=tekst1)
        elif second_currency == 'PLN':
            wynik2=self.dict_currency_and_values[first_currency]*ilosc
            tekst2 = str(round(wynik2, 2)) + " " + self.dict_currency_and_code[second_currency]
            self.finish_result.config(text=tekst2)
        else:
            wynik3=self.dict_currency_and_values[first_currency]*ilosc/self.dict_currency_and_values[second_currency]
            tekst3 = str(round(wynik3, 2)) + " " + self.dict_currency_and_code[second_currency]
            self.finish_result.config(text=tekst3)

    def field_to_displaying_the_result(self):
        result = Label(self.master, text="Po przewalutowaniu: ", bg="#c2efc2")
        result.config(font=("Olympic", 12))
        result.place(x=20, y=380)
        self.finish_result=Label(self.master, text="", bg="#c2efc2")
        self.finish_result.config(font=("Impact", 15))
        self.finish_result.place(x=200, y=380)


