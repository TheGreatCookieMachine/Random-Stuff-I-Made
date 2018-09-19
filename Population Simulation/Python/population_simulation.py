import time
import random
from tkinter import Tk, Label


window = Tk()
window.title('Population Simulation')
window.resizable(width = False, height = False)
window.geometry('500x100')

year = 0
population = 100
base_birth_rate = 0.0186
base_death_rate = 0.0078
good_year = 0
while True:
    yearly_birth_rate = base_birth_rate * (random.randint(90, 110) / 100)
    yearly_death_rate = base_death_rate * (random.randint(90, 110) / 100)
    if random.randint(1, 100) <= 10: #Bad Year
        yearly_death_rate = yearly_death_rate * 2
        yearly_birth_rate = yearly_birth_rate / 2
    elif random.randint(1, 100) <= 10 and good_year == 0: #Good Year
        yearly_birth_rate = yearly_birth_rate * 2
        yearly_death_rate = yearly_death_rate / 2
        good_year = 10
    population = round(population + (population * yearly_birth_rate) - (population * yearly_death_rate))
    year = year + 1
    lbl = Label(window, text = 'Population: ' + str(population) + '\nYear: ' + str(year), anchor="w")
    lbl.grid(column = 0, row = 0)
    window.update()
    if good_year > 0: #Ensures at least 10 years pass in between Good Years
        good_year = good_year - 1
    time.sleep(0.05)
window.mainloop()
