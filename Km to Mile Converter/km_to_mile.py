from tkinter import *


def button_click():
    km = entry.get()
    miles = round(int(km) * 0.62, 3)
    label_result.config(text=miles)


window = Tk()
window.title("Km to Miles Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)
window.eval('tk::PlaceWindow . center')

label_km = Label(text="Km")
label_km.grid(column=2, row=0)
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=1)
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

entry = Entry(width=7)
entry.grid(column=1, row=0)

label_result = Label(text=0)
label_result.grid(column=1, row=1)


window.mainloop()
