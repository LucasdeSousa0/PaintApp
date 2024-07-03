from tkinter import Frame, Button

class ColorPicker:
    def __init__(self, parent, app):
        color_box_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        color_box_frame.grid(row=0, column=2)

        Button(color_box_frame, text="Select Color", width=10, command=app.select_color).grid(row=0, column=0)
