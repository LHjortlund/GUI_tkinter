import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 500)

#create a label
my_label = tkinter.Label(text= "I am a label", font=("Arial", 24, "bold"))
my_label.pack()

#overwrite exciting label
my_label["text"] = "New Text"
my_label.config(text = "New Text")

#create a funktion to the button
def button_cliked():
    print("Button clicked")

#create a button
button = tkinter.Button(text="Click Me!", command=button_cliked)
button.pack()




window.mainloop()