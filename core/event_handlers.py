import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, EventType
from tkinter import Frame, Canvas, StringVar, IntVar
import PIL.ImageGrab as ImageGrab  


class EventHandlers:
    """Handles all user input events."""
    def __init__(self, app):
        self.app = app

    def bind_events(self, canvas):
        canvas.bind("<B1-Motion>", self.app.state_manager.paint)
        canvas.bind("<ButtonRelease-1>", self.app.state_manager.reset_point)
        canvas.bind("<B3-Motion>", self.app.state_manager.paint_right)
        canvas.bind("<Button-2>", self.app.state_manager.write_text)

    