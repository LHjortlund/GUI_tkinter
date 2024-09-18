import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 500)

#create a label
my_label = tkinter.Label(text= "I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")


window.mainloop()