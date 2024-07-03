import tkinter as tk
from tkinter import Frame, Canvas

from ui.toolbar import Toolbar
from ui.size_selector import SizeSelector
from ui.color_picker import ColorPicker
from ui.color_buttons import ColorButtons
from ui.save_clear import SaveAndClear
from ui.help_menu import HelpMenu
from ui.text_entry import TextEntry
from core.event_handlers import EventHandlers
from core.state_management import StateManager

class PaintApp:

    """Main application class for the Paint App.

    This class initializes the main window and all UI components,
    binds events, and contains the main application logic.
    """


    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("1100x600")
        self.root.resizable(False, False)

        self.canvas = Canvas(self.root, height=500, width=1100, bg="white")
        self.canvas.grid(row=1, column=0)


        self.state_manager = StateManager(self.canvas)
        self.event_handlers = EventHandlers(self)

        frame1 = Frame(self.root, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky='nw')

        Toolbar(frame1, self)
        SizeSelector(frame1, self)
        ColorPicker(frame1, self)
        ColorButtons(frame1, self)
        SaveAndClear(frame1, self)
        HelpMenu(frame1, self)
        TextEntry(frame1, self)

        self.event_handlers.bind_events(self.canvas)
        

    def run(self):
        """Start the Tkinter event loop."""

        self.root.mainloop()

    