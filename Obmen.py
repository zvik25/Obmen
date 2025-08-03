import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

# import pprint
#
# result = requests.get('https://open.er-api.com/v6/latest/USD') #request of data
# data = json.loads(result.text) # to get json format data
# p = pprint.PrettyPrinter(intent=4)
#
# p.print(data) #печатает в столбик данные json файла. Печать print() - в одну строчку вывод данных json файла.


def update_c_label(event): # обновление будет происходить при наступлении события - выбор из выпадающего списка
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)



def exchange():
    # code = entry.get()
    code = combobox.get()

    if code: #проверка для введенного значения кода
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status() #проверка доступности-работы сайта
            data = response.json()
            if code in data['rates']: #проверка кода валюты - есть, правильно - rates is from json
                exchange_rate = data['rates'][code] #code here is a key - for json file data
                c_name = cur[code] #для вывода названия валюты в сообщении ниже
                # mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {code} за 1 доллар')# .2f - два знака после запятой. {code} - в сообщение попадает код валюты
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {c_name} за 1 доллар')# .2f - два знака после запятой. В сообщение попадает название валюты
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена!')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')

    else: # if code not entered
        mb.showwarning('Внимание', "Введите код валюты.")

cur = {
    'RUB': 'Российский рубль',
    'BGP': 'Британский фунт стерлингов',
    'EUR': 'Евро',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар'
} #словарь вместо списка


"""Создаем оконный интерфейс"""
window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

# Label(text='Введите код валюты').pack(padx=10, pady=10) #не будет использоваться => переменную не задаем
Label(text='Выберите код валюты').pack(padx=10, pady=10) #не будет использоваться => переменную не задаем #For combobox

# cur = ['RUB', 'BGP', 'EUR', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD'] #список кодов для combobox'a #из этого
# списка сделали словарь для расшифровки кода валют

# combobox = ttk.Combobox(values=cur)
combobox = ttk.Combobox(values=list(cur.keys())) #создание списка из словаря
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_c_label) #на событие "выбор combobox" будет обновляться надпись на с_label

c_label = ttk.Label() #для расшифровки кода валюты
c_label.pack(padx=10, pady=10)

# entry=Entry() # не нужны из-за combobox
# entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)


window.mainloop()


