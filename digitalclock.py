from tkinter import Tk, Label


window = Tk()
window.title("Digital clock")
window.geometry("600x300")
window.configure(bg="steel blue")

label = Label(window, text="welcome", font=(
    "Arial Black", 78, "bold"), bg="steel blue", fg="white")
label.pack(pady=100)
window.mainloop()
