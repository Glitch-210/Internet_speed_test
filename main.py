import speedtest
from tkinter import *

# Speed Check Function
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + " MBps"  # Download speed in Mbps
    upload = str(round(sp.upload()/(10**6), 3)) + " MBps"  # Upload speed in Mbps
    lab_down.config(text=down)
    lab_up.config(text=upload)

# GUI Setup
sp = Tk()
sp.title("Internet Speed By OOBLA")
sp.geometry("500x500")
sp.config(bg="white")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 23, "bold"), bg="white", fg="black")
lab.place(x=60, y=40, height=40, width=380)

lab = Label(sp, text="Downloading Speed", font=("Time New Roman", 23, "bold"), fg="black", bg="pink")
lab.place(x=60, y=130, height=40, width=350)

lab_down = Label(sp, text="00", font=("Time New Roman", 16, "bold"), fg="white", bg="blue")
lab_down.place(x=160, y=200, height=40, width=150)

lab = Label(sp, text="Uploading Speed", font=("Time New Roman", 23, "bold"), fg="black", bg="pink")
lab.place(x=60, y=280, height=40, width=350)

lab_up = Label(sp, text="00", font=("Time New Roman", 16, "bold"), fg="white", bg="blue")
lab_up.place(x=160, y=340, height=40, width=150)

button = Button(sp, text="Check Speed", font=("Time New Roman", 15, "bold"), fg="brown", bg="cyan", relief=RAISED, command=speedcheck)
button.place(x=140, y=440, height=40, width=200)

sp.mainloop()