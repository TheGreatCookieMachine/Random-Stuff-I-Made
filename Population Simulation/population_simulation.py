from tkinter import *


window = Tk()
window.title('Population Simulation')
window.resizable(width = False, height = False)
window.geometry('500x100')

year = 1
population = 100
yearly_population_growth = 0.011
while True:
    population = round(population + (population * yearly_population_growth))
    year = year + 1
    lbl = Label(window, text = 'Population: ' + str(population), anchor="w")
    lbl.grid(column = 0, row = 0)
    lbl = Label(window, text = 'Year: ' + str(year), anchor="w")
    lbl.grid(column = 0, row = 1)
    window.update()
window.mainloop()
