from tkinter import *
import tkinter as tk
from tkinter import messagebox as msb
from PIL import ImageTk, Image, ImageOps

class main(object):
    time = 0

    def __init__(self):
         
        self.__root = Tk()
        title = Label(self.__root, text="Battleship", font=("Arial", 50))
        self.__root.title(title)

        APP_MIN_WIDTH = 1000
        APP_MIN_HEIGHT = 600
        APP_MAX_WIDTH = 1000
        APP_MAX_HEIGHT = 600
        self.__root.minsize(APP_MIN_WIDTH,
                            APP_MIN_HEIGHT)
        self.__root.maxsize(APP_MAX_WIDTH,
                            APP_MAX_HEIGHT)
        self.__root.protocol("WM_DELETE_WINDOW", self.on_exit_button_pressed)

        ## Putting the background image
        self.__bg = Image.open("Python1DProjectSC04TeamE\images\image.jpg")
        self.__bg = ImageOps.fit(self.__bg, (APP_MIN_HEIGHT, APP_MIN_HEIGHT))
        self.__bg = ImageTk.PhotoImage(self.__bg)
        self.__bg_label = Label(self.__root, image=self.__bg)
        self.__bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        ## Setting Main Frame
    def start(self):
        """
        Starts the mainloop
        :return: None
        """
        self.__root.mainloop()

    def on_exit_button_pressed(self):
        if msb.askokcancel("Quit", "Do you want to quit?"):
            self.__root.destroy()


master = main()

master.start()

