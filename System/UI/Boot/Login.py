from argparse import Action
from tkinter import Button, Entry, Label
from System.Utils.Utils import print_error, print_info, print_log, print_warning

from System.Utils.Colormap import White
from System.Utils.Utils import Asset

__author__ = 'MohammadGhadimiAzad'
__version__ = '1.0'

# Specific Colors
Login_background_color = "#477afb"
Login_entry_color = "#071F2B"
Login_Password_Entry = None
Login_UserName_Entry = None

def Login(master):  # Display the login window

    global Login_GUI, Login_Button_icon

    master.configure(background = Login_background_color)  # Sets the background to Blue

    Login_GUI = Asset("Login2.png")
    Login = Label(master, image = Login_GUI, borderwidth="0.1")
    Login.place(x=0, y=0)

    # UserName entry (username)
    global Login_UserName_Entry
    Login_UserName_Entry = Entry(
        Login,
        width = 29,
        #show = "•",
        borderwidth = "0.1",
        fg = "White",
        background = Login_entry_color,
        font = ("Segou UI", 10)
    )

    Login_UserName_Entry.config(insertbackground= White)
    Login_UserName_Entry.insert(0,"pc1") # the best userName
    Login_UserName_Entry.focus()
    Login_UserName_Entry.place(x= 411, y= 293)


    # Login entry (Password)
    global Login_Password_Entry
    Login_Password_Entry = Entry(
        Login,
        width = 29,
        show = "•",
        borderwidth = "0.1",
        fg = "White",
        background = Login_entry_color,
        font = ("Segou UI", 10)
    )

    Login_Password_Entry.config(insertbackground= White)
    Login_Password_Entry.insert(0,"123") # the best password
    Login_Password_Entry.place(x= 411, y= 332)


    Login_Button_icon = Asset("Login_btn.png")
    Login_Button = Button(Login,
        width = 66,
        height = 24,
        borderwidth = "0",
        relief = "raised",
        image = Login_Button_icon,
        command = login
    )
    Login_Button.place(x = 486, y = 370)

def login():
    global Login_Password_Entry
    global Login_UserName_Entry

    if (Login_Password_Entry.get() == "123"):
        from System.Core.Network import Network
        from System.Core.Core import GlobalObjects
        from System.UI.Boot.Desktop import Desktop

        GlobalObjects().set_settings(Login_UserName_Entry.get())
        Desktop(GlobalObjects().os)
        Network()
    else:
        print_warning("Error in login, Not match userName & Password")