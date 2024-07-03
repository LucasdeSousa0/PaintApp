from tkinter import Frame, Button, Label

class Toolbar:
    def __init__(self, parent, app):
        tools_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        tools_frame.grid(row=0, column=0)

        Button(tools_frame, text="Pencil", width=10, command=app.use_pencil).grid(row=0, column=0)
        Button(tools_frame, text="Eraser", width=10, command=app.use_eraser).grid(row=1, column=0)
        Label(tools_frame, text="Tools", width=10).grid(row=2, column=0)
