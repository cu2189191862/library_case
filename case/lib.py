import tkinter as tk
import time
from threading import Timer
# from win32api import GetSystemMetrics
# screen_width = GetSystemMetrics(0)
# screen_height = GetSystemMetrics(1)

information = {"library Chinese name" : "台大圖書館", "library English name" : "NTU library"}


class App(tk.Frame):
    def __init__(self, master=None): #constructor
        tk.Frame.__init__(self, master)
        self.root = master
        self.root.title("managing prog.")
        self.root.geometry("800x600")
        self.pack()
        self.bind_id_enter = None
        logInPage(self.root)

class logInPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.draw()
        self.read_input()

    def draw(self):
        #####top#################
        self.t1 = tk.Label(self)
        self.t2 = tk.Label(self)
        self.t1.config(text=information["library Chinese name"], width=100, height=2)
        self.t2.config(text=information["library English name"], bg="green", width=100, height=2)
        self.t1.pack()
        self.t2.pack()
        #####top end#############

        #######body###############
        self.t3 = tk.Label(self)
        self.t3.config(text="智慧預約書架系統", width=20, height=10, font=30)
        self.t3.pack()

        self.t4 = tk.Label(self)
        self.t4.config(text="查詢預約書請刷卡！", width=20, height=10, font=20)
        self.t4.pack()
        #######body end###########

    def switch(self, x):
        print("switching to showColorPage")
        self.destroy()
        self.master.unbind("<Return>", self.bind_id_enter)
        showColorPage(self.master)

    def read_input(self):
        self.bind_id_enter = root.bind("<Return>", self.switch)



class showColorPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.draw()
        self.switch()
    
    def draw(self):
        self.t1 = tk.Label(self)
        self.t2 = tk.Label(self)
        self.t1.config(text="this is show color page", width=100, height=2)
        self.t2.config(text="ha", bg="green", width=100, height=2)
        self.t1.pack()
        self.t2.pack()

    def switch(self):
        print("switching to detailPage")
        self.destroy_countDown = Timer(5.0, self.destroy)
        self.newPage_countDown = Timer(5.0, detailPage, [self.master])
        self.destroy_countDown.start()
        self.newPage_countDown.start()

class detailPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.draw()
        self.switch()
    
    def draw(self):
        self.t1 = tk.Label(self)
        self.t2 = tk.Label(self)
        self.t1.config(text="this is detail page", width=100, height=2)
        self.t2.config(text="ha", bg="green", width=100, height=2)
        self.t1.pack()
        self.t2.pack()

    def switch(self):
        print("switching to reminderPage")
        self.destroy_countDown = Timer(5.0, self.destroy)
        self.newPage_countDown = Timer(5.0, reminderPage, [self.master])
        self.destroy_countDown.start()
        self.newPage_countDown.start()


class reminderPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack()
        self.draw()
        self.switch()
    
    def draw(self):
        self.t1 = tk.Label(self)
        self.t2 = tk.Label(self)
        self.t1.config(text="this is reminder page", width=100, height=2)
        self.t2.config(text="ha", bg="green", width=100, height=2)
        self.t1.pack()
        self.t2.pack()

    def switch(self):
        print("switching to logInPage")
        self.destroy_countDown = Timer(5.0, self.destroy)
        self.newPage_countDown = Timer(5.0, logInPage, [self.master])
        self.destroy_countDown.start()
        self.newPage_countDown.start()


root = tk.Tk()

app = App(master=root)
app.mainloop()
