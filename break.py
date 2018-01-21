import tkinter as Tk
import tkinter.font
import time

class Window:
    def __init__(self):
        self.root = None
        self.hide = 45 #minutes
        self.hide = self.hide*60
        self.show = 60 #seconds


    def close(self):
        self.root.destroy()
        return

    def skip(self):
        self.root.destroy()
        time.sleep(self.hide)
        self.new()
    
    def tick(self):
        #print('Inside tick')
        self.x-=1
        if self.x >= 0:
            self.canvas.itemconfig(self.clock, text=str(self.x))
            self.canvas.itemconfig(self.arc, extent=359.9 + 6*self.x)
        # calls itself every 1000 milliseconds
        # to update the time display as needed
        self.canvas.after(1000, self.tick)

    def new(self):
        self.x = 60
        self.clock = None
        self.canvas = None
        self.arc = None
        self.root = Tk.Tk()
        self.root.overrideredirect(True)
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.configure(bg='black')
        self.root.wm_attributes("-alpha", 0.95)
        self.root.bind("<Escape>", lambda e: self.skip())
        fontobj = tkinter.font.Font(size = 25)
        fontobj2 = tkinter.font.Font(size = 85)
        self.canvas = Tk.Canvas(self.root, bg = 'black', height = self.root.winfo_screenheight(), width = self.root.winfo_screenwidth(), highlightthickness=1)
        msg  = self.canvas.create_text(687,160,text = "Hey Jay,\nIt's been 45 mins since your last break..\n Relax your eyes for 60 seconds..", font = fontobj, fill = 'white', justify = 'center')
        self.canvas.pack(fill = 'both',expand = True)
        xy = 585,261,785,461 
        self.arc = self.canvas.create_arc(xy, start = 90, extent = -359.9, style = 'arc', outline = 'white', width = 7, fill = 'yellow') 
        self.clock = self.canvas.create_text(687,360,text = '60', font = fontobj2, fill = 'white', justify = 'center')
        self.tick()
        self.root.after(self.show*1000, self.loop)

    def loop(self):
        if self.root:
            self.root.destroy()
        time.sleep(self.hide)
        self.new()
        self.root.mainloop()
        return

Window().loop()