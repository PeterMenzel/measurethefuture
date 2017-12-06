
from tkinter import *
from tkinter import ttk
import os
# import Image, ImageTk
# from Pillow import ImageTk, Image
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
from PIL import ImageTk, Image
import PIL


YEARS = ["2017", "2018", "2019", "2020"]
MONTHS = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = ["1", "2", "3", "4", "5"]
HOURS = ["9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM"]

class MeasureTheFutureApp:

    def __init__(self, master):

        master.title('Measure The Future - Townsville CityLibraries')

        self.header_frame = ttk.Frame(master)
        self.header_frame.pack(side = TOP)
        self.selection_frame = ttk.Frame(master)
        self.selection_frame.pack(side = LEFT)
        self.presentation_frame = ttk.Frame(master)
        self.presentation_frame.pack(side = RIGHT)
        self.presentation_frame.config(padding = (30, 15))

        self.year_label = ttk.Label(self.selection_frame, text = "Year:")
        self.year_label.grid(row = 0, column = 0)
        self.month_label = ttk.Label(self.selection_frame, text = "Month:")
        self.month_label.grid(row = 1, column = 0)
        self.day_label = ttk.Label(self.selection_frame, text = "Day:")
        self.day_label.grid(row = 2, column = 0)
        self.hour_label = ttk.Label(self.selection_frame, text = "Hour:")
        self.hour_label.grid(row = 3, column = 0)
        print(self.year_label.config())

        # logo = PhotoImage(file = "/Users/localadmin/PycharmProjects/measurethefuture/interface/11_29_0830/scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3 2")
        # os.chdir('11_29_0830')
        # print(os.listdir('.')[0])
        # logo = PhotoImage(file = "{}/{}".format(os.getcwd(), os.listdir('.')[0]))
        # self.presentation_frame.config(image = logo)

        # self.scout_cam_image = self.get_scout_cam_image().subsample(2, 2)
        # self.scout_cam_label = Label(self.presentation_frame)
        # self.scout_cam_label.pack()
        # self.scout_cam_label.img = self.scout_cam_image
        # self.scout_cam_label.config(image = self.scout_cam_label.img)

        os.chdir('11_29_0830')
        # print(os.getcwd())
        print(os.listdir('.')[2])
        self.scout_cam_image = Image.open(os.listdir('.')[2])
        # self.scout_cam_image = self.scout_cam_image.resize((800, 250), Image.ANTIALIAS)
        self.scout_cam_canvas = Canvas(self.presentation_frame)
        self.scout_cam_canvas.config(width = 680, height = 480)
        print(self.scout_cam_canvas.config())
        self.scout_cam_canvas.image = PIL.ImageTk.PhotoImage(self.scout_cam_image)
        self.scout_cam_canvas.create_image(0, 0, image=self.scout_cam_canvas.image, anchor='nw', tags="IMG")
        self.scout_cam_canvas.pack()
        # img = Image.open("flower.png")
        self.scout_cam_canvas.bind("<Configure>", self.resize)

        ttk.Label(self.presentation_frame, text = "Visitors: ").pack()

        year = StringVar()
        self.year_combobox = ttk.Combobox(self.selection_frame, textvariable = year)
        self.year_combobox.config(values = YEARS)
        self.year_combobox.grid(row = 0, column = 1)

        month = StringVar()
        self.month_combobox = ttk.Combobox(self.selection_frame, textvariable = month)
        self.month_combobox.config(values = MONTHS)
        self.month_combobox.grid(row = 1, column = 1)

        day = StringVar()
        self.day_combobox = ttk.Combobox(self.selection_frame, textvariable = day)
        self.day_combobox.config(values = DAYS)
        self.day_combobox.grid(row = 2, column = 1)

        hour = StringVar()
        self.hour_combobox = ttk.Combobox(self.selection_frame, textvariable = hour)
        self.hour_combobox.config(values = HOURS)
        self.hour_combobox.grid(row = 3, column = 1)

        # rescale all the objects tagged with the "all" tag
        # self.scale("all", 0, 0)


    def get_scout_cam_image(self):
        os.chdir('11_29_0830')
        # print(os.getcwd())
        print(os.listdir('.'))
        return PhotoImage(file = "{}/{}".format(os.getcwd(), os.listdir('.')[0]))
        # return PhotoImage(file = "/Users/localadmin/PycharmProjects/measurethefuture/interface/11_29_0830/scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3.gif")
        # return PhotoImage(file = "scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3.gif")
        # return ImageTk.PhotoImage(Image.open("{}/{}".format(os.getcwd(), os.listdir('.')[0])))
        # return Image(os.listdir('.')[0], "Scout Cam Image")
        # return Image.open(os.listdir('.')[0])

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.scout_cam_image.resize(size,Image.ANTIALIAS)
        self.scout_cam_canvas.image = ImageTk.PhotoImage(resized)
        self.scout_cam_canvas.delete("IMG")
        self.scout_cam_canvas.create_image(0, 0, image=self.scout_cam_canvas.image, anchor=NW, tags="IMG")


def main():

    root = Tk()
    app = MeasureTheFutureApp(root)
    root.mainloop()

if __name__ == "__main__": main()