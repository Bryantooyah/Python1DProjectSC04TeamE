from tkinter import *
import tkinter as tk
from tkinter import messagebox as msb

class main(object):
    time = 0

    def __init__(self):
         
        self.__root = Tk()
        self.__root.title("Battleship")

        APP_MIN_WIDTH = 1000
        APP_MIN_HEIGHT = 600
        APP_MAX_WIDTH = 1000
        APP_MAX_HEIGHT = 600
        self.__root.minsize(APP_MIN_WIDTH,
                            APP_MIN_HEIGHT)
        self.__root.maxsize(APP_MAX_WIDTH,
                            APP_MAX_HEIGHT)
        self.__root.protocol("WM_DELETE_WINDOW", self.on_exit_button_pressed)


