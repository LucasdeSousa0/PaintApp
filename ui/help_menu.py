from tkinter import Frame, Button

class HelpMenu:
    def __init__(self, parent, app):
        help_setting_frame = Frame(parent, height=100, width=100, relief='sunken', borderwidth=3)
        help_setting_frame.grid(row=0, column=5)

        Button(help_setting_frame, text="Help", width=10, command=app.state_manager.show_help).grid(row=0, column=0)
        Button(help_setting_frame, text="Settings", width=10, command=app.state_manager.show_settings).grid(row=1, column=0)
        Button(help_setting_frame, text="About", width=10, command=app.state_manager.show_about).grid(row=2, column=0)
