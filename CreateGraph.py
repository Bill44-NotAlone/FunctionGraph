import matplotlib.pyplot as plt
import numexpr as ne
from tkinter import *
from functools import partial

coord = None

def stringToFunction(functionsrt, x0, x1):
    x = []
    while x0 < x1:
        x.append(x0)
        x0 = x0 + 0.01
    for i in x:
        c = ne.evaluate(functionsrt)
    return([x, c])
def BuildGraph(coord):
    x = coord[0]
    y = coord[1]

    for i in range(0, len(x)-1):
        plt.plot([x[i],x[i+1]],[y[i], y[i+1]], 'b')

    plt.title('График функции.')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)

    plt.show()

def Clik(text, ex0, ex1):
    x0 = float(ex0.get())
    x1 = float(ex1.get())
    text = text.get()
    coord = stringToFunction(text, x0, x1)
    BuildGraph(coord)

if(__name__ == '__main__'):
    window = Tk()
    window.title("Программное построение графиков.")
    entryfun = Entry(window, width = 40, justify = CENTER)
    entryx0 = Entry(window, width = 20, justify = CENTER)
    entryx1 = Entry(window, width = 20, justify = CENTER)
    entryfun.pack(side = LEFT)
    entryx0.pack(side = LEFT)
    entryx1.pack(side = LEFT)
    btn = Button(window, width = 40, text="Расчитать график.", command=partial(Clik, entryfun, entryx0, entryx1))
    btn.pack()
    window.mainloop()
    #coord=stringToFunction("cos(x * x) + tan(x)", 2, 10)
    #BuildGraph(coord)

