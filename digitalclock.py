from tkinter import Tk, Label
from datetime import datetime


window = Tk()
window.title("Digital clock")
window.geometry("600x300")
window.configure(bg="steel blue")

label = Label(window, text="welcome", font=(
    "Arial Black", 78, "bold"), bg="steel blue", fg="white")
label.pack(pady=100)


def clock():
    time = datetime.now().strftime("%H: %M: %S")
    date = datetime.now().strftime("%D: %M: %Y")
    label.configure(text=time)
    label.after(500, clock)


clock()
window.mainloop()
