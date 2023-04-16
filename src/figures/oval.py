from tkinter import Canvas
from src.figures.figure import Figure

class Oval(Figure):
    
     def draw(self, canvas: Canvas):
        canvas.create_oval(
            self.coords, 
            outline=self.options['lineColor'],
            fill=self.options['backgroundColor'],  
            width=self.options['depth']
        )