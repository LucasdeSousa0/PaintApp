from tkinter import Frame, Button, Label
from core.event_handlers import EventHandlers
from core.state_management import StateManager

class Toolbar:
    """Toolbar component containing drawing tools like pencil and eraser.

    Attributes:
        parent (Frame): The parent widget that contains this toolbar.
        app (PaintApp): Reference to the main application class.
    """
    def __init__(self, parent, app):
        """Initialize the Toolbar with a reference to the main app and its parent frame."""

        tools_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        tools_frame.grid(row=0, column=0)

        Button(tools_frame, text="Pencil", width=10, command=app.state_manager.use_pencil).grid(row=0, column=0)
        Button(tools_frame, text="Eraser", width=10, command=app.state_manager.use_eraser).grid(row=1, column=0)
        Label(tools_frame, text="Tools", width=10).grid(row=2, column=0)
