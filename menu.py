from tkinter import *
import tkinter as tk
from tkinter import messagebox as msb

class startFrame(object):

    def __init__(self, context):
        self.__context = context
        self.__frame = self.__create_frame(self.__context.get_root())

    def __on_submit_button_pressed(self):  # Button to submit the name
        name = self.__name_entry.get().strip()
        if name:  # Ensure name is not empty
            print(f"Name submitted: {name}")
            self.__context.set_name(name)  # Save name in the main class
            self.__context.on_submit_button_pressed()  # Switch to menu frame
        else:
            print("Please enter a valid name.")


    def __on_exit_button_pressed(self):  # Button to show exit dialog
        print("startFrame: Exit button clicked...")
        self.__context.on_exit_button_pressed()

    def __create_frame(self, root):

        frame = Frame(root,
                      padx=10,
                      pady=10,
                      highlightthickness=1,
                      highlightbackgroun="#CCCCCC",)

        Label(frame,
              text= "Battle Ships!!",
              pady=5,
              font="time 14 bold").pack()

        # User Name Entry
        Label(frame, text="Enter your name:").pack()
        self.__name_entry = Entry(frame)
        self.__name_entry.pack()

        # Buttons
        bt_submit = Button(frame, text="Submit", width=10, command=self.__on_submit_button_pressed)
        bt_submit.pack()

        bt_exit = Button(frame, text="Exit", width=20, padx=4, command=self.__on_exit_button_pressed)
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
    
class menuFrame(object):
    def __init__(self, context):
        self.__context = context
        self.__frame = self.__create_frame(self.__context.get_root())

    def __on_singleplayer_button_pressed(self):  # Button to start singleplayer game
        print("MenuFrame: Single player button clicked...")
        self.__context.on_singleplayer_button_pressed()

    def __on_twoplayer_button_pressed(self):  # Button to start 2 players game
        print("MenuFrame: Two player button clicked...")
        self.__context.on_twoplayer_button_pressed()

    def __on_highscore_button_pressed(self):  # Button to show highscore
        print("MenuFrame: Highscore button clicked...")
        self.__context.on_highscore_button_pressed()

    def __on_setting_button_pressed(self):
        print("MenuFrame: Setting button clicked...")
        self.__context.on_setting_button_pressed()

    def __on_exit_button_pressed(self):  # Button to show exit dialog
        print("MenuFrame: Exit button clicked...")
        self.__context.on_exit_button_pressed()

    def __create_frame(self, root):
        frame = Frame(root,
                      padx=10,
                      pady=10,
                      highlightthickness=1,
                      highlightbackgroun="#CCCCCC",)
        
        naming = self.__context.name
        Label(frame,
              text= f"Welcome Back, {naming}!",
              pady=5,
              font="time 14 bold").pack()

        # Single player button
        bt_singleplayer = Button(frame,
                                 text= "Single Player",
                                 width=20,
                                 padx=4,
                                 takefocus="tab",
                                 command=self.__on_singleplayer_button_pressed)
        
        # Two player button
        bt_twoplayer = Button(frame,
                              text= "Two Player",
                              width=20,
                              padx=4,
                              takefocus="tab",
                              command=self.__on_twoplayer_button_pressed)
        
        # Highscore button
        bt_highscore = Button(frame,
                              text= "Highscore",
                              width=20,
                              padx=4,
                              takefocus="tab",
                              command=self.__on_highscore_button_pressed)
        # Setting button
        bt_setting = Button(frame,
                            text= "Setting",
                            width=20,
                            padx=4,
                            takefocus="tab",
                            command=self.__on_setting_button_pressed)
        
        # Exit button
        bt_exit = Button(frame,
                         text= "Exit",
                         width=20,
                         padx=4,
                         command=self.__on_exit_button_pressed)

        # Packing buttons
        bt_singleplayer.pack()
        bt_twoplayer.pack()
        bt_highscore.pack()
        bt_setting.pack()
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
    
