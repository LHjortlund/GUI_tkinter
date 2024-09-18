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
#make the input the new text
def button_cliked():
    print("Button clicked")
    new_text = input.get()
    my_label.config(text = new_text)

#create a button
button = tkinter.Button(text="Click Me!", command=button_cliked)
button.pack()

#entry component
input = tkinter.Entry(width=10)
input.pack()
print(input.get())




window.mainloop()