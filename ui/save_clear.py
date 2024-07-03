from tkinter import Frame, Button

class SaveAndClear:
    def __init__(self, parent, app):
        save_image_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        save_image_frame.grid(row=0, column=4)

        Button(save_image_frame, text="Save", width=10, command=app.save_image).grid(row=0, column=0)
        Button(save_image_frame, text="New", width=10, command=app.create_new).grid(row=1, column=0)
        Button(save_image_frame, text="Clear", width=10, command=app.clear).grid(row=2, column=0)
