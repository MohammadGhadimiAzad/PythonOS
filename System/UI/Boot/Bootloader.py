from tkinter import Label, PhotoImage

from System.Utils.Colormap import Black
from System.Utils.Utils import Asset, print_log, Asset_colored
from System.Utils.Vars import Assets_directory

__author__ = 'MohammadGhadimiAzad'
__version__ = '1.5'

def Boot_loader(master):

    print_log("Starting...")

    global Logon

    master.configure(background=Black)  # Set the background color to black.

    Logon = Asset_colored("logon.png", 1)
    Boot_Logo = Label(master, image=Logon, borderwidth=0.1)

    Boot_Logo.place(x= 408, y= 160)

    # Animation...
    frames_count = 27 # Frames per second

    # Make a list of frames
    frames = [
        PhotoImage(file= Assets_directory + "/GUI/Bootloader/Loading.gif", format="gif -index %i" % (i))
        for i in range(frames_count)
    ]

    # Show and update the frames
    def update(ind):

        frame = frames[ind]
        ind += 1

        if ind == frames_count:
            ind = 0

        loading.configure(image=frame)
        master.after(50, update, ind)

    loading = Label(master, borderwidth=0.1)
    loading.place(x= 480, y= 400)

    def End_bootloader():

        Boot_Logo.place_forget()
        loading.place_forget()

        print_log("Finishing...")

    master.after(1, update, 0)

    master.after(10000, End_bootloader)
