import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox, EventType
from tkinter import Frame, Canvas, StringVar, IntVar
import PIL.ImageGrab as ImageGrab  

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("1100x600")
        self.root.resizable(False, False)

        self.stroke_size = IntVar(value=1)
        self.stroke_color = StringVar(value="black")
        self.previousColor = StringVar(value="white")
        self.previousColor2 = StringVar(value="white")
        self.textValue = StringVar()
        self.prevPoint = [0, 0]
        self.currentPoint = [0, 0]

        self.setup_ui()

    def setup_ui(self):
        frame1 = Frame(self.root, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky='nw')

        from .toolbar import Toolbar
        from .size_selector import SizeSelector
        from .color_picker import ColorPicker
        from .color_buttons import ColorButtons
        from .save_clear import SaveAndClear
        from .help_menu import HelpMenu
        from .text_entry import TextEntry

        Toolbar(frame1, self)
        SizeSelector(frame1, self)
        ColorPicker(frame1, self)
        ColorButtons(frame1, self)
        SaveAndClear(frame1, self)
        HelpMenu(frame1, self)
        TextEntry(frame1, self)

        self.canvas = Canvas(self.root, height=500, width=1100, bg="white")
        self.canvas.grid(row=1, column=0)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_point)
        self.canvas.bind("<B3-Motion>", self.paint_right)
        self.canvas.bind("<Button-2>", self.write_text)

    def run(self):
        self.root.mainloop()

    def use_pencil(self):
        self.stroke_color.set("black")
        self.canvas["cursor"] = "pencil"

    def use_eraser(self):
        self.stroke_color.set("white")
        self.canvas["cursor"] = "dotbox"

    def select_color(self):
        selected_color = colorchooser.askcolor(title="Select Color")
        if selected_color[1] is not None:
            self.stroke_color.set(selected_color[1])
            self.previousColor2.set(self.previousColor.get())
            self.previousColor.set(selected_color[1])

    def paint(self, event):
        x, y = event.x, event.y
        self.currentPoint = [x, y]
        if self.prevPoint != [0, 0]:
            self.canvas.create_line(self.prevPoint[0], self.prevPoint[1], x, y, fill=self.stroke_color.get(), width=self.stroke_size.get())
        self.prevPoint = [x, y]

    def reset_point(self, event):
        self.prevPoint = [0, 0]

    def paint_right(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x + self.stroke_size.get(), y + self.stroke_size.get(), fill=self.stroke_color.get(), outline=self.stroke_color.get())

    def write_text(self, event):
        self.canvas.create_text(event.x, event.y, text=self.textValue.get(), fill=self.stroke_color.get())

    def save_image(self):
        file_location = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_location:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            img = ImageGrab.grab(bbox=(x, y, x + 1100, y + 500))
            img.save(file_location)
            if messagebox.askyesno("Paint App", "Do you want to open the image?"):
                img.show()

    def clear(self):
        if messagebox.askokcancel("Paint App", "Do you want to clear everything?"):
            self.canvas.delete('all')

    def create_new(self):
        if messagebox.askyesno("Paint App", "Do you want to save before you clear everything?"):
            self.save_image()
        self.clear()

    def show_help(self):
        help_text = ("1. Draw by holding the left mouse button to draw lines.\n"
                     "2. Hold the right mouse button to draw ovals.\n"
                     "3. Click the middle mouse button to put text on the Canvas.\n"
                     "4. Use the toolbar to select tools like Pencil or Eraser.")
        messagebox.showinfo("Help", help_text)

    def show_settings(self):
        messagebox.showwarning("Settings", "Not Available")

    def show_about(self):
        messagebox.showinfo("About", "This Paint App is created using Python and Tkinter.")
