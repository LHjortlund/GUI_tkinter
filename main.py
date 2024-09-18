import tkinter

#create a funktion to the button
#make the input the new text
def button_cliked():
    print("Button clicked")
    new_text = input.get()
    my_label.config(text = new_text)

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(500, 500)
window.config(padx=20, pady=20) #you can add space around your widgets so it has some space

#create a label
my_label = tkinter.Label(text= "I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

#overwrite exciting label
my_label["text"] = "New Text"
my_label.config(text = "New Text")

#new button
new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

#create a button
button = tkinter.Button(text="Click Me!", command=button_cliked)
button.grid(column=1, row=1)

#Entry component
input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=3, row=3)



window.mainloop()