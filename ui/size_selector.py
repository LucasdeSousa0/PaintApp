from tkinter import Frame, Button, OptionMenu, Label

class SizeSelector:
    """Component for selecting the size of the brush/pen.

    Attributes:
        parent (Frame): The parent widget that contains this size selector.
        app (PaintApp): Reference to the main application class.
    """

    def __init__(self, parent, app):
        """Initialize the size selector with options."""

        size_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        size_frame.grid(row=0, column=1)

        Button(size_frame, text="Default", width=10, command=app.state_manager.use_pencil).grid(row=0, column=0)
        OptionMenu(size_frame, app.state_manager.stroke_size, *[1, 2, 3, 4, 5, 10]).grid(row=1, column=0)
        Label(size_frame, text="Size", width=10).grid(row=2, column=0)
