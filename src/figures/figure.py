from tkinter import Canvas

class Figure:
    def __init__(self, coords, options):
        self.coords = coords
        self.options = options


    def draw(self, canvas: Canvas):
        canvas.create_polygon(
            self.coords, 
            fill=self.options['backgroundColor'], 
            outline=self.options['lineColor'], 
            width=self.options['depth']
        )