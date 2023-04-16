from tkinter import Canvas
from src.figures.figure import Figure

class Circle(Figure):
    def __init__(self, center, radius, options):
        self.radius = radius
        self.options = options
        super().__init__(center, options)
        

    def draw(self, canvas: Canvas):
        x = self.coords[0]
        y = self.coords[1]
        canvas.create_oval(
            (x - self.radius),
            (y - self.radius),
            (x + self.radius),
            (y + self.radius),
            outline=self.options['lineColor'],
            fill=self.options['backgroundColor'],  
            width=self.options['depth']
        )
        