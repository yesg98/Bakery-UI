import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text="샌드위치 (5000원)").grid(column=0, row=0)
        Label(window, text="케이크 (20000원)").grid(column=0, row=1)
        self.senNum_entry = Entry(window, width=10)
        self.cakNum_entry = Entry(window, width=10)
        self.senNum_entry.grid(column=1, row=0)
        self.cakNum_entry.grid(column=1, row=1)
        res_button = Button(window, text="주문하기", command=self.send_order)
        res_button.grid(column=0, row=2)

    def send_order(self):
        order_text = ""
        self.senNum = self.senNum_entry.get()
        self.cakNum = self.cakNum_entry.get()
        if str(self.senNum).isdigit():
            sen = int(self.senNum)
        else:
            sen = 0
        if str(self.cakNum).isdigit():
            cak = int(self.cakNum)
        else:
            cak = 0
        if sen > 0:
            if cak > 0:
                order_text += self.name + \
                    ": 샌드위치 (5000원) "+str(sen) + \
                    "개, 케이크 (20000원) "+str(cak)+"개"
            else:
                order_text += self.name + \
                    ": 샌드위치 (5000원) "+str(sen)+"개"
        else:
            if cak > 0:
                order_text += self.name + \
                    ": 케이크 (20000원) "+str(cak)+"개"
            else:
                return
        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
