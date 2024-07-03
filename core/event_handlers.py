import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, EventType
from tkinter import Frame, Canvas, StringVar, IntVar
import PIL.ImageGrab as ImageGrab  


class EventHandlers:
    """Handles all user input events."""
    def __init__(self, app):
        self.app = app

    def bind_events(self, canvas):
        event_actions = {
            "<B1-Motion>": self.app.state_manager.paint,
            "<ButtonRelease-1>": self.app.state_manager.reset_point,
            "<B3-Motion>": self.app.state_manager.paint_right,
            "<Button-2>": self.app.state_manager.write_text,
        }
        for event, action in event_actions.items():
            canvas.bind(event, action)

    