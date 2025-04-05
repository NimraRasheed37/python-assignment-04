import tkinter as tk

# Problem Statement
# Implement an 'eraser' on a canvas.

class Canvas:
    def __init__(self):
        self.width = 600
        self.height = 600
        self.title = "Eraser Canvas"
        self.color = "red"
        self.cells = []
        self.create_canvas()
        self.create_cells()
        self.canvas.bind("<B1-Motion>", self.erase)

    def create_canvas(self):
        self.canvas = tk.Canvas(width=self.width, height=self.height, bg=self.color)
        self.canvas.pack()

    def create_cells(self):
        for x in range(0, self.width, 10):
            for y in range(0, self.height, 10):  # Fixed `height` to `self.height`
                self.cells.append(self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=self.color))

    def run(self):
        self.canvas.mainloop()

    def erase(self, event):
        x = event.x
        y = event.y
        for cell in self.cells:
            coords = self.canvas.coords(cell)
            if coords[0] < x < coords[2] and coords[1] < y < coords[3]:
                self.canvas.itemconfig(cell, fill="white")


class Eraser:
    def __init__(self, canvas):
        self.canvas = canvas.canvas  # Access the canvas object
        self.width = 20
        self.height = 20
        self.color = "black"
        self.create_eraser()

    def create_eraser(self):
        self.eraser = self.canvas.create_rectangle(0, 0, self.width, self.height, fill=self.color)
        self.canvas.tag_bind(self.eraser, "<B1-Motion>", self.move)

    def move(self, event):
        x = event.x
        y = event.y
        self.canvas.coords(self.eraser, x, y, x + self.width, y + self.height)


def main():
    # Create canvas
    canvas = Canvas()

    # Create eraser
    eraser = Eraser(canvas)

    # Run the canvas
    canvas.run()


if __name__ == "__main__":
    main()


