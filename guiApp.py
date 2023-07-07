import tkinter as tk
from source import * 

def submit():
    skift = skiftlag[var.get()-1]

    gl = float(input1.get())

    p_tot = dagslon(gl)
   
    startdatum = input2.get()
    startdatum = startdatum.split("-")
    startdatum = datetime(int(startdatum[0]), int(startdatum[1]), int(startdatum[2]))
    
    slutdatum = input3.get()
    slutdatum = slutdatum.split("-")
    slutdatum = datetime(int(slutdatum[0]), int(slutdatum[1]), int(slutdatum[2]))

    skillnad = relativedelta(slutdatum, startdatum)
    
    ddag = skillnad.days
    dmon = skillnad.months + ddag/30

    summa = lon_summa(startdatum, slutdatum, skift.ref_datum, skift.startperiod, skift.startdag, p_tot)

    if skift and gl and startdatum and slutdatum:
        result_label.config(text=f"Intjänade pengar: {round(summa*1.12)}kr \nBrutto: {round(summa*1.12*0.67)}kr \nGenomsnittlig månadslön: {round((summa*1.12)/dmon)}kr")
    else:
        result_label.config(text="Fyll i alla val.")

def reset():
    var.set(0)
    input1.delete(0, tk.END)
    input2.delete(0, tk.END)
    input3.delete(0, tk.END)
    result_label.config(text="Please fill in all choices and inputs.")


# Create the Tkinter window
window = tk.Tk()
window.title("LÖNEUTRÄKNARE")

# Create a Tkinter variable to store the selected option
var = tk.IntVar()

# Create the radio buttons
option1 = tk.Radiobutton(window, text="Lag 1", variable=var, value=1)
option2 = tk.Radiobutton(window, text="Lag 2", variable=var, value=2)
option3 = tk.Radiobutton(window, text="Lag 3", variable=var, value=3)
option4 = tk.Radiobutton(window, text="Lag 4", variable=var, value=4)
option5 = tk.Radiobutton(window, text="Lag 5", variable=var, value=5)

# Create the input labels and entry fields
input_label1 = tk.Label(window, text="Timlön i kr:")
input1 = tk.Entry(window)

input_label2 = tk.Label(window, text="Startdatum yyyy-mm-dd:")
input2 = tk.Entry(window)

input_label3 = tk.Label(window, text="Slutdatum yyyy-mm-dd:")
input3 = tk.Entry(window)

# Create the submit button
submit_btn = tk.Button(window, text="Visa lön", command=submit)

reset_btn = tk.Button(window, text="Återställ", command=reset)

# Create the result label
result_label = tk.Label(window, text="Här visas din slutgilltiga lön för den givna period", font=("Arial", 12, "bold"))

# Place the radio buttons in the window
option1.pack()
option2.pack()
option3.pack()
option4.pack()
option5.pack()

# Place the input elements in the window
input_label1.pack()
input1.pack()

input_label2.pack()
input2.pack()

input_label3.pack()
input3.pack()

# Place the submit button and result label in the window
submit_btn.pack()
reset_btn.pack()
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
