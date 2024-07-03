from tkinter import Frame, Button

class ColorPicker:
    """Component for selecting the color of the brush/pen.

    Attributes:
        parent (Frame): The parent widget that contains this color picker.
        app (PaintApp): Reference to the main application class.
    """
    def __init__(self, parent, app):
        """Initialize the color picker with options."""

        color_box_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        color_box_frame.grid(row=0, column=2)

        Button(color_box_frame, text="Select Color", width=10, command=app.select_color).grid(row=0, column=0)
