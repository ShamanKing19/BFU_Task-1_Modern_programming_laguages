import json
from tkinter import *
from src.figures.circle import Circle
from src.figures.triangle import Triangle
from src.figures.square import Square
from src.figures.polygon import Polygon
from src.figures.line import Line
from src.figures.oval import Oval
from pprint import pprint


class App:
    dataPath = 'data.json'
    windowWidth = 800
    windowHeight = 600
    canvasBackground = 'white'


    def run(self):
        figuresData = self.readData()
        figures = self.createFigures(figuresData)
        window = self.createWindow()
        canvas = self.createCanvas(window)
        for figure in figures:
            figure.draw(canvas)

        window.mainloop()
        

    def createCanvas(self, window) -> Canvas:
        canvas = Canvas(window, width = self.windowWidth, height = self.windowHeight, bg = self.canvasBackground)
        canvas.pack()

        return canvas


    def createWindow(self) -> Tk:
        window = Tk()
        window.geometry(f'{self.windowWidth}x{self.windowHeight}')

        return window


    def createFigures(self, figuresData) -> list: 
        figures = []
        for figure in figuresData:
            type = figure['figure']
            options = figure['options']
            commonOptions = figure['commonOptions']

            if type == 'round':
                figures.append(Circle(options['center'], options['radius'], commonOptions))
            elif type == 'triangle':
                figures.append(Triangle(options['coords'], commonOptions))
            elif type == 'square':
                figures.append(Square(options['coords'], commonOptions))
            elif type == 'polygon':
                figures.append(Polygon(options['coords'], commonOptions))
            elif type == 'line':
                figures.append(Line(options['coords'], commonOptions))
            elif type == 'oval':
                figures.append(Oval(options['coords'], commonOptions))
            

        return figures

    
    def readData(self) -> list:
        try:
            with open(self.dataPath, 'r') as file:
                data = json.loads(file.read())
                figures = data.get('figures', False)
                if figures:
                    return figures
                
                return []
        except:
            print(f'File {self.dataPath} not found!')
            return []
