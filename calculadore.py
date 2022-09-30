from tkinter import *
from tkinter import ttk
import math
import requests
import pandas as pd

root = Tk()
root.title('Calculadora Com Crip/USD')
root.geometry('+550+230')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

operador = ''
entry1 = StringVar()
entry2 = StringVar()


def clear():
    global operador
    operador = ''
    entry2.set('0')


def clear_one():
    global operador
    operador = operador[:-1]
    if operador == '':
        entry2.set('0')
    else:
        entry2.set(operador)


def click(button):
    global operador
    operador += str(button)
    entry2.set(operador)


def result():
    global operador
    try:
        res = str(eval(operador))
    except:
        res = 'ERROR'
    entry2.set(res)


def call_api(name):
    url_api = ' https://ftx.com/api'
    api = '/markets'
    url = url_api + api
    markets = requests.get(url).json()
    data = markets['result']
    df = pd.DataFrame(data)
    price = df[df['name'] == name].price
    return price


def convert_to_dollar():
    global operador
    val = operador.split()
    quantity = float(val[0])
    price = float(call_api(val[1]))
    dollars = str(quantity * price)
    entry2.set(dollars)


def conver_to_cripto():
    global operador
    val = operador.split()
    quantity = float(val[0])
    price = float(call_api(val[1]))
    dollars = str(quantity / price)
    entry2.set(dollars)


def temaOscuro(*args):
    style.configure('mainframe.TFrame', background='#010924')
    style.configure('label1.TLabel', background='#010924', foreground='white')
    style.configure('label2.TLabel', background='#010924', foreground='white')
    style.configure('button_num.TButton', background='#00044A', foreground='white')
    style.configure('button_cls.TButton', background='#010924', foreground='white')
    style.configure('button_fal.TButton', background='#010924', foreground='white')


def temaClaro(*args):
    style.configure('mainframe.TFrame', background='#DBDBDB')
    style.configure('label1.TLabel', background='#DBDBDB', foreground='black')
    style.configure('label2.TLabel', background='#DBDBDB', foreground='black')
    style.configure('button_num.TButton', background='#EDEDFA', foreground='black')
    style.configure('button_cls.TButton', background='#DBDBDB', foreground='black')
    style.configure('button_fal.TButton', background='#DBDBDB', foreground='black')


style = ttk.Style()
style.theme_use('clam')
style.configure('mainframe.TFrame', background='#DBDBDB')

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.grid(column=0, row=0, sticky='WNES')

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)

style_lab1 = ttk.Style()
style_lab1.configure('label1.TLabel', font='arial 15', anchor='E')

lab_entry1 = ttk.Label(mainframe, textvariable=entry1, style='label1.TLabel')
lab_entry1.grid(column=0, row=0, columnspan=4, sticky='WNES')

style_lab2 = ttk.Style()
style_lab2.configure('label2.TLabel', font='arial 40', anchor='E')

lab_entry2 = ttk.Label(mainframe, textvariable=entry2, style='label2.TLabel')
lab_entry2.grid(column=0, row=1, columnspan=1, sticky='WNES')

style_but = ttk.Style()
style_but.configure('button_num.TButton', font='arial 22', width=5, background='#FFFFFF', relief='flat')
style_but.map('button_num.TButton', foreground=[('active', '#5134FF')])

style_cls = ttk.Style()
style_cls.configure('button_cls.TButton', font='arial 22', width=5, background='#CECECE', relief='flat')
style_cls.map('button_cls.TButton', foreground=[('active', '#FF0000')])

style_fal = ttk.Style()
style_fal.configure('button_fal.TButton', font='arial 22', width=5, background='#CECECE', relief='flat')
style_fal.map('button_fal.TButton', foreground=[('active', '#26ADFF')])

button0 = ttk.Button(mainframe, text='0', style='button_num.TButton', command=lambda: click(0))
button1 = ttk.Button(mainframe, text='1', style='button_num.TButton', command=lambda: click(1))
button2 = ttk.Button(mainframe, text='2', style='button_num.TButton', command=lambda: click(2))
button3 = ttk.Button(mainframe, text='3', style='button_num.TButton', command=lambda: click(3))
button4 = ttk.Button(mainframe, text='4', style='button_num.TButton', command=lambda: click(4))
button5 = ttk.Button(mainframe, text='5', style='button_num.TButton', command=lambda: click(5))
button6 = ttk.Button(mainframe, text='6', style='button_num.TButton', command=lambda: click(6))
button7 = ttk.Button(mainframe, text='7', style='button_num.TButton', command=lambda: click(7))
button8 = ttk.Button(mainframe, text='8', style='button_num.TButton', command=lambda: click(8))
button9 = ttk.Button(mainframe, text='9', style='button_num.TButton', command=lambda: click(9))

clear()
button_cls = ttk.Button(mainframe, text=chr(9003), style='button_cls.TButton', command=lambda: clear_one())
button_allcls = ttk.Button(mainframe, text='C', style='button_cls.TButton', command=lambda: clear())
button_par1 = ttk.Button(mainframe, text='(', style='button_fal.TButton', command=lambda: click('('))
button_par2 = ttk.Button(mainframe, text=')', style='button_fal.TButton', command=lambda: click(')'))
button_point = ttk.Button(mainframe, text='.', style='button_fal.TButton', command=lambda: click('.'))

button_mul = ttk.Button(mainframe, text='x', style='button_fal.TButton', command=lambda: click('*'))
button_div = ttk.Button(mainframe, text=chr(247), style='button_fal.TButton', command=lambda: click('/'))
button_rest = ttk.Button(mainframe, text='-', style='button_fal.TButton', command=lambda: click('-'))
button_sum = ttk.Button(mainframe, text='+', style='button_fal.TButton', command=lambda: click('+'))

button_equ = ttk.Button(mainframe, text='=', style='button_fal.TButton', command=result)
button_conv_d = ttk.Button(mainframe, text='($)', style='button_fal.TButton', command=lambda: convert_to_dollar())
button_conv_c = ttk.Button(mainframe, text='(C)', style='button_fal.TButton', command=lambda: conver_to_cripto())
button_quar = ttk.Button(mainframe, text='√', style='button_fal.TButton', command=lambda: click('math.sqrt'))

button_btc = ttk.Button(mainframe, text='BTC', style='button_fal.TButton',
                        command=lambda: click(' BTC/USD'))
button_eth = ttk.Button(mainframe, text='ETH', style='button_fal.TButton',
                        command=lambda: click(' ETH/USD'))
button_usdt = ttk.Button(mainframe, text='USDT', style='button_fal.TButton',
                         command=lambda: click(' USDT/USD'))
button_bnb = ttk.Button(mainframe, text='BNB', style='button_fal.TButton',
                        command=lambda: click(' BNB/USD'))

button_par1.grid(column=0, row=2, sticky='WNES')
button_par2.grid(column=1, row=2, sticky='WNES')
button_allcls.grid(column=2, row=2, sticky='WNES')
button_cls.grid(column=3, row=2, sticky='WNES')
button7.grid(column=0, row=3, sticky='WNES')
button8.grid(column=1, row=3, sticky='WNES')
button9.grid(column=2, row=3, sticky='WNES')
button_div.grid(column=3, row=3, sticky='WNES')
button4.grid(column=0, row=4, sticky='WNES')
button5.grid(column=1, row=4, sticky='WNES')
button6.grid(column=2, row=4, sticky='WNES')
button_mul.grid(column=3, row=4, sticky='WNES')
button1.grid(column=0, row=5, sticky='WNES')
button2.grid(column=1, row=5, sticky='WNES')
button3.grid(column=2, row=5, sticky='WNES')
button_sum.grid(column=3, row=5, sticky='WNES')
button0.grid(column=0, row=6, columnspan=2, sticky='WNES')
button_point.grid(column=2, row=6, sticky='WNES')
button_rest.grid(column=3, row=6, sticky='WNES')
button_equ.grid(column=0, row=7, sticky='WNES')
button_conv_d.grid(column=1, row=7, sticky='WNES')
button_conv_c.grid(column=2, row=7, sticky='WNES')
button_quar.grid(column=3, row=7, sticky='WNES')
button_bnb.grid(column=0, row=8, sticky='WNES')
button_btc.grid(column=1, row=8, sticky='WNES')
button_usdt.grid(column=2, row=8, sticky='WNES')
button_eth.grid(column=3, row=8, sticky='WNES')

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-d>', temaOscuro)
root.bind('<KeyPress-l>', temaClaro)

root.mainloop()
