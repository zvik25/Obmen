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
    code = t_combobox.get()
    name = cur[code]
    c_label.config(text=name)



def exchange():
    # code = entry.get()
    # code = t_combobox.get()
    t_code = t_combobox.get()
    b_code = b_combobox.get()

    if t_code and b_code: #проверка для введенного значения кода
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')#для доллара только
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status() #проверка доступности-работы сайта
            data = response.json()
            if t_code in data['rates']: #проверка кода валюты - есть, правильно - rates is from json
                exchange_rate = data['rates'][t_code] #code here is a key - for json file data
                t_name = cur[t_code] #для вывода названия валюты в сообщении ниже
                b_name = cur[b_code]
                # mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {code} за 1 доллар')# .2f - два знака после запятой. {code} - в сообщение попадает код валюты
                mb.showinfo('Курс обмена', f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')# .2f - два знака после запятой. В сообщение попадает название валюты
            else:
                mb.showerror('Ошибка', f'Валюта {t_code} не найдена!')
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
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'
} #словарь вместо списка


"""Создаем оконный интерфейс"""
window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x300')

# Label(text='Введите код валюты').pack(padx=10, pady=10) #не будет использоваться => переменную не задаем
Label(text='Базовая валюта').pack(padx=10, pady=10) #не будет использоваться => переменную не задаем #For combobox
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)


Label(text='Целевая валюта').pack(padx=10, pady=10) #не будет использоваться => переменную не задаем #For combobox

# cur = ['RUB', 'BGP', 'EUR', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD'] #список кодов для combobox'a #из этого
# списка сделали словарь для расшифровки кода валют

# combobox = ttk.Combobox(values=cur)
t_combobox = ttk.Combobox(values=list(cur.keys())) #создание списка из словаря
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<<ComboboxSelected>>', update_c_label) #на событие "выбор combobox" будет обновляться надпись на с_label

c_label = ttk.Label() #для расшифровки кода валюты
c_label.pack(padx=10, pady=10)

# entry=Entry() # не нужны из-за combobox
# entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)


window.mainloop()


