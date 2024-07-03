from tkinter import Frame, Label, Entry, Button

class TextEntry:
    """
    Provides a text entry widget for users to input text that can be added to the canvas.

    Attributes:
        parent (Frame): The parent widget that houses the text entry component.
        app (PaintApp): Reference to the main application to access shared resources and methods.
    """
    def __init__(self, parent, app):
        text_frame = Frame(parent, height=100, width=200, relief='sunken', borderwidth=3)
        text_frame.grid(row=0, column=6)

        Label(text_frame, text="Write your Text here:", width=20).grid(row=0, column=0)
        Entry(text_frame, textvariable=app.state_manager.textValue, width=20).grid(row=1, column=0)
        Button(text_frame, text="Clear", width=20, command=lambda: app.state_manager.textValue.set("")).grid(row=2, column=0)
