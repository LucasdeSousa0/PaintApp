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
        
        self.previousColor = StringVar()
        self.previousColor.set("white")
        
        self.previousColor2 = StringVar()
        self.previousColor2.set("white")

        self.textValue = StringVar()

        self.prevPoint = [0, 0]
        self.currentPoint = [0, 0]

        frame1 = Frame(self.root, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky=NW)
        
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
        self.canvas.bind("<ButtonRelease-1>", self.paint)
        self.canvas.bind("<B3-Motion>", self.paint_right)
        self.canvas.bind("<Button-2>", self.write_text)

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
            self.previousColor2.set(self.previousColor.get())
            self.previousColor.set(selected_color[1])

            self.previousColorButton["bg"] = self.previousColor.get()
            self.previousColor2Button["bg"] = self.previousColor2.get()

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
    def __init__(self, parent, app):
        tools_frame = Frame(parent, height=100, width=100, relief=SUNKEN, borderwidth=3)
        tools_frame.grid(row=0, column=0)

        pencil_button = Button(tools_frame, text="Pencil", width=10, command=app.use_pencil)
        pencil_button.grid(row=0, column=0)
        eraser_button = Button(tools_frame, text="Eraser", width=10, command=app.use_eraser)
        eraser_button.grid(row=1, column=0)
        Label(tools_frame, text="Tools", width=10).grid(row=2, column=0)

class SizeSelector:
    def __init__(self, parent, app):
        size_frame = Frame(parent, height=100, width=100, relief=SUNKEN, borderwidth=3)
        size_frame.grid(row=0, column=1)

        Button(size_frame, text="Default", width=10, command=app.use_pencil).grid(row=0, column=0)
        OptionMenu(size_frame, app.stroke_size, *[1, 2, 3, 4, 5, 10]).grid(row=1, column=0)
        Label(size_frame, text="Size", width=10).grid(row=2, column=0)

class ColorPicker:
    def __init__(self, parent, app):
        color_box_frame = Frame(parent, height=100, width=100, relief=SUNKEN, borderwidth=3)
        color_box_frame.grid(row=0, column=2)

        Button(color_box_frame, text="Select Color", width=10, command=app.select_color).grid(row=0, column=0)
        app.previousColorButton = Button(color_box_frame, text="Previous", width=10, command=lambda: app.stroke_color.set(app.previousColor.get()))
        app.previousColorButton.grid(row=1, column=0)
        app.previousColor2Button = Button(color_box_frame, text="Previous2", width=10, command=lambda: app.stroke_color.set(app.previousColor2.get()))
        app.previousColor2Button.grid(row=2, column=0)

class ColorButtons:
    def __init__(self, parent, app):
        colors_frame = Frame(parent, height=100, width=200, relief=SUNKEN, borderwidth=3)
        colors_frame.grid(row=0, column=3)

        colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
        for i, color in enumerate(colors):
            Button(colors_frame, text=color, bg=color.lower(), width=10, command=lambda c=color.lower(): app.stroke_color.set(c)).grid(row=i//2, column=i%2)

class SaveAndClear:
    def __init__(self, parent, app):
        save_image_frame = Frame(parent, height=100, width=100, relief=SUNKEN, borderwidth=3)
        save_image_frame.grid(row=0, column=4)

        Button(save_image_frame, text="Save", width=10, command=app.save_image).grid(row=0, column=0)
        Button(save_image_frame, text="New", width=10, command=app.create_new).grid(row=1, column=0)
        Button(save_image_frame, text="Clear", width=10, command=app.clear).grid(row=2, column=0)

class HelpMenu:
    def __init__(self, parent, app):
        help_setting_frame = Frame(parent, height=100, width=100, relief=SUNKEN, borderwidth=3)
        help_setting_frame.grid(row=0, column=5)

        Button(help_setting_frame, text="Help", width=10, command=app.show_help).grid(row=0, column=0)
        Button(help_setting_frame, text="Settings", width=10, command=app.show_settings).grid(row=1, column=0)
        Button(help_setting_frame, text="About", width=10, command=app.show_about).grid(row=2, column=0)

class TextEntry:
    def __init__(self, parent, app):
        text_frame = Frame(parent, height=100, width=200, relief=SUNKEN, borderwidth=3)
        text_frame.grid(row=0, column=6)

        Label(text_frame, text="Write your Text here:", width=20).grid(row=0, column=0)
        Entry(text_frame, textvariable=app.textValue, width=20).grid(row=1, column=0)
        Button(text_frame, text="Clear", width=20, command=lambda: app.textValue.set("")).grid(row=2, column=0)

if __name__ == "__main__":
    app = PaintApp()
    app.run()