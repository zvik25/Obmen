import requests
import json
from tkinter import *
from tkinter import messagebox as mb

# import pprint
#
# result = requests.get('https://open.er-api.com/v6/latest/USD') #request of data
# data = json.loads(result.text) # to get json format data
# p = pprint.PrettyPrinter(intent=4)
#
# p.print(data) #печать в столбик данных json файла. Печать print() - в одну строчку вывод данных json файла.
"""Создаем оконный интерфейс"""


window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Введите код валюты').pack(padx=10, pady=10) #не будет использоваться => переменную не задаем

entry=Entry()
entry.pack(padx=10, pady=10)

Button(text'Получить курс обмена к доллару', command=exchange.pack(padx=10, pady=10))


window.mainloop()


