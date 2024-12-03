from tkinter import *
import tkinter as tk
from tkinter import messagebox as msb

class MenuFrame(object):

    def __init__(self, context):
        self.__context = context
        #self.__frame = self.__create_frame(self.__context.get_root())

    def __on_start_button_pressed(self):  # Button to start new game
        print("The game has started...")
        self.__context.on_start_arrange_button_pressed()

    def __on_help_button_pressed(self):  # Button to show help section
        print("MenuFrame: Help button pressed")
        self.__context.on_help_button_pressed()

    def __on_exit_button_pressed(self):  # Button to show exit dialog
        print("MenuFrame: Exit button clicked...")
        self.__context.on_exit_button_pressed()

    def __create_frame(self, root):

        frame = Frame(root,
                      padx=10,
                      pady=10,
                      highlightthickness=1,
                      highlightbackgroun="#CCCCCC",)

        Label(frame,
              text= "Menu Title",
              pady=5,
              font="time 14 bold").pack()

        # Start game button
        bt_start_game = Button(frame,
                               text= "Start Game",
                               width=20,
                               padx=4,
                               takefocus="tab",
                               command=self.__on_start_button_pressed)
        # Help button
        bt_help = Button(frame,
                         text= "Help",
                         width=20,
                         padx=4,
                         command=self.__on_help_button_pressed)
        # Exit button
        bt_exit = Button(frame,
                         text= "Exit",
                         width=20,
                         padx=4,
                         command=self.__on_exit_button_pressed)

        # Packing buttons
        bt_start_game.pack()
        bt_help.pack()
        bt_exit.pack()

        return frame

    def place_frame(self):
        self.__frame.place(relx=0.17,
                           rely=0.3,
                           anchor=CENTER)

    def displace_frame(self):
        self.__frame.place_forget()

    def get_frame(self):
        return self.__frame