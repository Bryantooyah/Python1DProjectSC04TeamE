from tkinter import *
import tkinter as tk
from tkinter import messagebox as msb
from PIL import ImageTk, Image, ImageOps

import menu
import singleplayer 
import two_player 
import highscore


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

        ## Username
        self.name = ""

        ## Putting the background image
        self.__bg = Image.open("Python1DProjectSC04TeamE\images\image.jpg")
        self.__bg = ImageOps.fit(self.__bg, (APP_MIN_HEIGHT, APP_MIN_HEIGHT))
        self.__bg = ImageTk.PhotoImage(self.__bg)
        self.__bg_label = Label(self.__root, image=self.__bg)
        self.__bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        ## Setting start frame
        self.__start_frame = menu.startFrame(self)
        self.__start_frame.place_frame()
        

    def start(self):
        """
        Starts the mainloop
        :return: None
        """
        self.__root.mainloop()

    def get_root(self):
        """
        :return: BaseWidget tkinter root (master)
        """
        return self.__root
    
    def set_name(self, name):
        self.name = name
        print(f"Name stored in main: {self.name}")

    def on_submit_button_pressed(self):
        self.__start_frame.displace_frame()
        self.__menu_frame = menu.menuFrame(self)
        self.__menu_frame.place_frame()

    def on_exit_button_pressed(self):
        if msb.askokcancel("Quit", "Do you want to quit?"):
            self.__root.destroy()
    
    def on_single_player_button_pressed(self):
        self.__menu_frame.displace_frame()
        self.__single_player_frame = singleplayer.singlePlayerFrame(self)
        self.__single_player_frame.place_frame()

    def on_twoplayer_button_pressed(self):
        self.__menu_frame.displace_frame()
        self.__two_player_frame = two_player.twoPlayerFrame(self)
        self.__two_player_frame.place_frame()
    
    def on_highscore_button_pressed(self):
        self.__menu_frame.displace_frame()
        self.__highscore_frame = highscore.highscoreFrame(self)
        self.__highscore_frame.place_frame()
    
    def on_setting_button_pressed(self):
        self.__menu_frame.displace_frame()
        self.__setting_frame = menu.settingFrame(self)
        self.__setting_frame.place_frame()
        



master = main()

master.start()

