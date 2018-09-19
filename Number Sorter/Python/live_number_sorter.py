import random
from tkinter import *

window = Tk()
window.title('Number Sorter')
window.resizable(width=False, height=False)
window.geometry('1280x720')

n = 0
low = 0
high = 0
process = []
result = []
counting = True

while counting is True:
    while len(process) < 1000:
        process.append(random.randint(1, 1000))
        lbl = Label(window, text=process, wraplength=1250, anchor="w")
        lbl.grid(column=0, row=0)
        window.update()
    while n < len(process):
        if process[n] > high:
            result.append(process[n])
            high = process[n]
            if low == 0:
                low = process[n]
            lbl = Label(window, text=result, wraplength=1250, anchor="w")
            lbl.grid(column=0, row=1)
            window.update()
        elif process[n] < low:
            result.insert(0, process[n])
            low = process[n]
            lbl = Label(window, text=result, wraplength=1250, anchor="w")
            lbl.grid(column=0, row=1)
            window.update()
        else:
            n2 = 0
            while True:
                if process[n] <= result[n2]:
                    result.insert(n2, process[n])
                    break
                n2 = n2 + 1
            lbl = Label(window, text=result, wraplength=1250, anchor="w")
            lbl.grid(column=0, row=1)
            window.update()
        n = n + 1
    counting = False
window.mainloop()
