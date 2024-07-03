from tkinter import Frame, Button

class SaveAndClear:
    """ 
    Provides buttons for saving the current canvas content, creating new canvases, and clearing the current canvas.

    Attributes:
        parent (Frame): The parent widget that houses the save and clear functionality.
        app (PaintApp): Reference to the main application to control file operations and canvas management.
    """

    def __init__(self, parent, app):
        save_image_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        save_image_frame.grid(row=0, column=4)

        Button(save_image_frame, text="Save", width=10, command=app.state_manager.save_image).grid(row=0, column=0)
        Button(save_image_frame, text="New", width=10, command=app.state_manager.create_new).grid(row=1, column=0)
        Button(save_image_frame, text="Clear", width=10, command=app.state_manager.clear).grid(row=2, column=0)
