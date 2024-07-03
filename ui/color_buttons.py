from tkinter import Frame, Button

class ColorButtons:
    """
    Provides a set of buttons for quick color selection in the Paint App.

    Attributes:
        parent (Frame): The parent widget that houses the color buttons.
        app (PaintApp): Reference to the main application to manage color state changes.
    """

    def __init__(self, parent, app):
        colors_frame = Frame(parent, height=100, width=200, relief='sunken', borderwidth=3)
        colors_frame.grid(row=0, column=3)

        colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
        for i, color in enumerate(colors):
            Button(colors_frame, text=color, bg=color.lower(), width=10, command=lambda c=color.lower(): app.state_manager.stroke_color.set(c)).grid(row=i//2, column=i%2)
