from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_value.get())
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles)


#button widget generator
b1=Button(window, text="Execute", command=km_to_miles)

#grid allows us to have more widget and lets us choose where we
#put things
b1.grid(row=0, column=0)

#instantiating the user entry placeholder
e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

#text widget
t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)

#b1.pack()


window.mainloop()