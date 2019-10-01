from tkinter import *

fen = Tk()
bouton = Button(fen, text="quitter", command=fen.destroy)
lab = Label(fen, text="Trololo")
champs = Entry(fen)
bouton2 = Button(fen, text="the big red button")
can = Canvas(fen, width =200, height =200, bg ="red")

def update():
    lab.config(text = "hello")

bouton2.config(command = update)

can.pack()
bouton.pack()
lab.pack()
champs.pack()
bouton2.pack()

fen.mainloop()