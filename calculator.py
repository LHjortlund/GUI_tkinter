import tkinter

window = tkinter.Tk()
window.title("Miles til kilometer omregner")
window.config(padx=20, pady=20)

def miles_to_km():
    miles = float(miles_input.get()) #henter brugerinput
    km = round(miles * 1.609) #omregner til kilometer og afrunder
    km_result.config(text=f"{km}") #opdatere tabel med resultatet

#Entry component til at indtaste miles
miles_input = tkinter.Entry(width=10)
print(miles_input.get())
miles_input.grid(column=2, row=1)

#Miles Label
label = tkinter.Label(text="Miles")
label.grid(column=3, row=1)

#label for "is equal to"
equal = tkinter.Label(text="is equal to")
equal.grid(column=1, row=2)

#lbael til at vise resultatet i kilometer
km_result = tkinter.Label(text="0")
km_result.grid(column=2, row=2)

#label for km
k_m = tkinter.Label(text="Km")
k_m.grid(column=3, row=2)

#Button der kalder miles_to_km-funktionen
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=3)

window.mainloop()