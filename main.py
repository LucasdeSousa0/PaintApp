from tkinter import *
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

class PaintApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Paint App")
        self.root.geometry("1100x600")

        self.stroke_size = IntVar()
        self.stroke_size.set(1)
        self.stroke_color = StringVar()
        self.stroke_color.set("black")

        self.textValue = StringVar()

        self.prevPoint = [0, 0]
        self.currentPoint = [0, 0]

        self.canvas = Canvas(self.root, height=500, width=1100, bg="white")
        self.canvas.grid(row=1, column=0)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.paint)
        self.canvas.bind("<B3-Motion>", self.paint_right)
        self.canvas.bind("<Button-2>", self.write_text)

        Toolbar(self)
        ColorPicker(self)
        SizeSelector(self)
        SaveAndClear(self)
        HelpMenu(self)

        self.root.resizable(False, False)

    def run(self):
        self.root.mainloop()

    def use_pencil(self):
        self.stroke_color.set("black")
        self.canvas["cursor"] = "arrow"

    def use_eraser(self):
        self.stroke_color.set("white")
        self.canvas["cursor"] = "dotbox"

    def select_color(self):
        selected_color = colorchooser.askcolor("blue", title="Select Color")
        if selected_color[1] is None:
            self.stroke_color.set("black")
        else:
            self.stroke_color.set(selected_color[1])

    def paint(self, event):
        x, y = event.x, event.y
        self.currentPoint = [x, y]
        if self.prevPoint != [0, 0]:
            self.canvas.create_line(self.prevPoint[0], self.prevPoint[1], x, y, fill=self.stroke_color.get(), width=self.stroke_size.get())
        self.prevPoint = [x, y]
        if event.type == EventType.ButtonRelease:
            self.prevPoint = [0, 0]

    def paint_right(self, event):
        x, y = event.x, event.y
        self.canvas.create_oval(x, y, x + self.stroke_size.get(), y + self.stroke_size.get(), fill=self.stroke_color.get(), outline=self.stroke_color.get())

    def save_image(self):
        try:
            file_location = filedialog.asksaveasfilename(defaultextension=".jpg")
            x = self.root.winfo_rootx()
            y = self.root.winfo_rooty() + 100
            img = ImageGrab.grab(bbox=(x, y, x + 1100, y + 500))
            img.save(file_location)
            if messagebox.askyesno("Paint App", "Do you want to open the image?"):
                img.show()
        except Exception as e:
            messagebox.showinfo("Paint app:", "Error occurred")

    def clear(self):
        if messagebox.askokcancel("Paint app", "Do you want to clear everything?"):
            self.canvas.delete('all')

    def create_new(self):
        if messagebox.askyesno("Paint app", "Do you want to save before you clear everything?"):
            self.save_image()
        self.clear()

    def show_help(self):
        help_text = ("1. Draw by holding the right button of the mouse to create dotted lines.\n"
                     "2. Click the scroll wheel to put text on the Canvas.\n"
                     "3. Click on Select Color to select a specific color\n"
                     "4. Click on Clear to clear the entire Canvas")
        messagebox.showinfo("Help", help_text)

    def show_settings(self):
        messagebox.showwarning("Settings", "Not Available")

    def show_about(self):
        messagebox.showinfo("About", "This paint app is the best!")

    def write_text(self, event):
        self.canvas.create_text(event.x, event.y, text=self.textValue.get())

class Toolbar:
    def __init__(self, app):
        self.frame = Frame(app.root, height=100, width=1100)
        self.frame.grid(row=0, column=0, sticky=NW)

        self.create_tools(app)

    def create_tools(self, app):
        tools_frame = Frame(self.frame, height=100, width=100, relief=SUNKEN, borderwidth=3)
        tools_frame.grid(row=0, column=0)

        pencil_button = Button(tools_frame, text="Pencil", width=10, command=app.use_pencil)
        pencil_button.grid(row=0, column=0)
        eraser_button = Button(tools_frame, text="Eraser", width=10, command=app.use_eraser)
        eraser_button.grid(row=1, column=0)
        Label(tools_frame, text="Tools", width=10).grid(row=3, column=0)

class ColorPicker:
    def __init__(self, app):
        self.frame = Frame(app.root, height=100, width=100, relief=SUNKEN, borderwidth=3)
        self.frame.grid(row=0, column=2)

        self.create_color_picker(app)

    def create_color_picker(self, app):
        Button(self.frame, text="Select Color", width=10, command=app.select_color).grid(row=0, column=0)
        
class SizeSelector:
    def __init__(self, app):
        self.frame = Frame(app.root, height=100, width=100, relief=SUNKEN, borderwidth=3)
        self.frame.grid(row=0, column=1)

        self.create_size_selector(app)

    def create_size_selector(self, app):
        Button(self.frame, text="Default", width=10, command=app.use_pencil).grid(row=0, column=0)
        OptionMenu(self.frame, app.stroke_size, *[1, 2, 3, 4, 5, 10]).grid(row=1, column=0)
        Label(self.frame, text="Size", width=10).grid(row=2, column=0)

class SaveAndClear:
    def __init__(self, app):
        self.frame = Frame(app.root, height=100, width=100, relief=SUNKEN, borderwidth=3)
        self.frame.grid(row=0, column=4)

        self.create_save_and_clear(app)

    def create_save_and_clear(self, app):
        Button(self.frame, text="Save", width=10, command=app.save_image).grid(row=0, column=0)
        Button(self.frame, text="New", width=10, command=app.create_new).grid(row=1, column=0)
        Button(self.frame, text="Clear", width=10, command=app.clear).grid(row=2, column=0)

class HelpMenu:
    def __init__(self, app):
        self.frame = Frame(app.root, height=100, width=100, relief=SUNKEN, borderwidth=3)
        self.frame.grid(row=0, column=5)

        self.create_help_menu(app)

    def create_help_menu(self, app):
        Button(self.frame, text="Help", width=10, command=app.show_help).grid(row=0, column=0)
        Button(self.frame, text="Settings", width=10, command=app.show_settings).grid(row=1, column=0)
        Button(self.frame, text="About", width=10, command=app.show_about).grid(row=2, column=0)

if __name__ == "__main__":
    app = PaintApp()
    app.run()