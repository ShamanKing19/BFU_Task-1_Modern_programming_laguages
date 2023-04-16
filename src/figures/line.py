from tkinter import Canvas
from src.figures.figure import Figure

class Line(Figure):
    
    def draw(self, canvas: Canvas):
        canvas.create_line(
            self.coords,
            fill=self.options['backgroundColor'],  
            width=self.options['depth']
        )