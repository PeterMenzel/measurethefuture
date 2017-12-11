
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
from datalist import DataList
from scout_summaries import ScoutSummaries


YEARS = ["2017", "2018", "2019", "2020"]
MONTHS = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = ["1", "2", "3", "4", "5"]
HOURS = ["9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM"]



#!/usr/bin/python

# simple.py

import wx
import wx.grid as gridlib


class MeasureTheFutureApp(wx.Frame):

    def __init__(self, parent, title):
        super(MeasureTheFutureApp, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()
        self.present_image()
        print(self.presentation_panel_size)

    def InitUI(self):


        # os.chdir('..')
        self.datalist = DataList("download (3)")
        print(os.getcwd())
        self.datalist.extract_files("download (3)")
        self.datalist.get_fixed_filename()
        self.datalist.load_scout_healths()
        self.datalist.load_scout_interactions()
        self.datalist.load_scout_summaries()


        main_panel = wx.Panel(self)
        main_panel_grid = wx.BoxSizer(wx.HORIZONTAL)

        # selection_panel = wx.Panel(frame)
        selection_panel = wx.Panel(main_panel)
        selection_box = wx.BoxSizer(wx.HORIZONTAL)
        self.presentation_panel = wx.Panel(main_panel)
        presentation_box = wx.BoxSizer(wx.VERTICAL)

        selection_grid = wx.FlexGridSizer(4, 2, 9, 25)

        year = wx.StaticText(selection_panel, label="Year:")
        month = wx.StaticText(selection_panel, label="Month:")
        day = wx.StaticText(selection_panel, label="Day:")
        hour = wx.StaticText(selection_panel, label="Hour:")

        year_combo = wx.ComboBox(selection_panel, choices=YEARS, style=wx.CB_READONLY)
        month_combo = wx.ComboBox(selection_panel, choices=MONTHS, style=wx.CB_READONLY)
        day_combo = wx.ComboBox(selection_panel, choices=DAYS, style=wx.CB_READONLY)
        hour_combo = wx.ComboBox(selection_panel, choices=HOURS, style=wx.CB_READONLY)

        selection_grid.AddMany([(year), (year_combo, 1, wx.EXPAND), (month),
                     (month_combo, 1, wx.EXPAND), (day), (day_combo, 1, wx.EXPAND),
                                (hour), (hour_combo, 1, wx.EXPAND)])

        # selection_grid.AddGrowableRow(2, 1)
        # selection_grid.AddGrowableCol(1, 1)
        # presentation_panel = wx.Panel(panel)

        selection_box.Add(selection_grid, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)

        self.presentation_panel_size = self.presentation_panel.GetSize()
        print(self.presentation_panel_size)
        self.scout_image = wx.Image(os.listdir('.')[0], wx.BITMAP_TYPE_ANY)
        # print(scout_image.Size())
        self.scout_image.Rescale(640, 360)
        # scout_image.Size(width=640, height=360)
        scout_image_control = wx.StaticBitmap(self.presentation_panel, wx.ID_ANY, wx.BitmapFromImage(self.scout_image))
        print(scout_image_control.Size)
        scout_image_control.SetBitmap(wx.BitmapFromImage(self.scout_image))

        myGrid = gridlib.Grid(self.presentation_panel)
        myGrid.CreateGrid(20, 20)
        myGrid.EnableGridLines(False)
        # myGrid.HideRowLabels()
        # myGrid.HideColLabels()
        # myGrid.GridWindow()
        myGrid.AutoSize()
        presentation_box.Add(myGrid, 1, wx.EXPAND | wx.ALL)

        presentation_box = wx.BoxSizer(wx.VERTICAL)
        presentation_box.Add(myGrid, 1, wx.EXPAND)

        for i in list(range(20)):
            for j in list(range(20)):
                myGrid.SetCellBackgroundColour(i, j, (255, 0, 0, 50))
                attr = gridlib.GridCellAttr()
                attr.SetReadOnly(True)
                myGrid.SetReadOnly(i, j, True)






        wx.StaticText(self.presentation_panel, label="Visitors: ")

        selection_panel.SetSizer(selection_box)
        self.presentation_panel.SetSizer(presentation_box)
        # panel_grid.Add(selection_panel, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        # panel_grid.Add(presentation_panel, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
        main_panel_grid.Add(selection_panel, 0, wx.EXPAND | wx.RIGHT, 5)
        main_panel_grid.Add(self.presentation_panel, 1, wx.EXPAND)
        # panel_grid.Add((3, -1))
        main_panel.SetSizer(main_panel_grid)

    def OnSize(self, event):
        self.presentation_panel_size = self.presentation_panel.GetSize()
        event.Skip()

    def present_image(self):
        pass





if __name__ == '__main__':
    app = wx.App()
    MeasureTheFutureApp(None, title='Measure The Future - Townsville CityLibraries')
    app.MainLoop()




# class MeasureTheFutureApp:
#
#     def __init__(self, master):




    # def get_scout_cam_image(self):
    #     os.chdir('download (3)')
    #     # print(os.getcwd())
    #     print(os.listdir('.'))
    #     return PhotoImage(file = "{}/{}".format(os.getcwd(), os.listdir('.')[0]))
        # return PhotoImage(file = "/Users/localadmin/PycharmProjects/measurethefuture/interface/11_29_0830/scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3.gif")
        # return PhotoImage(file = "scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3.gif")
        # return ImageTk.PhotoImage(Image.open("{}/{}".format(os.getcwd(), os.listdir('.')[0])))
        # return Image(os.listdir('.')[0], "Scout Cam Image")
        # return Image.open(os.listdir('.')[0])

    # def resize(self, event):
    #     size = (event.width, event.height)
    #     resized = self.scout_cam_image.resize(size,Image.ANTIALIAS)
    #     self.scout_cam_canvas.image = ImageTk.PhotoImage(resized)
    #     self.scout_cam_canvas.delete("IMG")
    #     self.scout_cam_canvas.create_image(0, 0, image=self.scout_cam_canvas.image, anchor=NW, tags="IMG")


# def main():
#
#     root = Tk()
#     app = MeasureTheFutureApp(root)
#     root.mainloop()

# if __name__ == "__main__": main()








# master.title('Measure The Future - Townsville CityLibraries')
#         print(os.getcwd())
#         self.header_frame = ttk.Frame(master)
#         self.header_frame.pack(side = TOP)
#         self.selection_frame = ttk.Frame(master)
#         self.selection_frame.pack(side = LEFT)
#         self.presentation_frame = ttk.Frame(master)
#         self.presentation_frame.pack(side = RIGHT)
#         self.presentation_frame.config(padding = (30, 15))
#
#         self.year_label = ttk.Label(self.selection_frame, text = "Year:")
#         self.year_label.grid(row = 0, column = 0)
#         self.month_label = ttk.Label(self.selection_frame, text = "Month:")
#         self.month_label.grid(row = 1, column = 0)
#         self.day_label = ttk.Label(self.selection_frame, text = "Day:")
#         self.day_label.grid(row = 2, column = 0)
#         self.hour_label = ttk.Label(self.selection_frame, text = "Hour:")
#         self.hour_label.grid(row = 3, column = 0)
#         print(self.year_label.config())
#
#         # logo = PhotoImage(file = "/Users/localadmin/PycharmProjects/measurethefuture/interface/11_29_0830/scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3 2")
#         # os.chdir('11_29_0830')
#         # print(os.listdir('.')[0])
#         # logo = PhotoImage(file = "{}/{}".format(os.getcwd(), os.listdir('.')[0]))
#         # self.presentation_frame.config(image = logo)
#
#         # self.scout_cam_image = self.get_scout_cam_image().subsample(2, 2)
#         # self.scout_cam_label = Label(self.presentation_frame)
#         # self.scout_cam_label.pack()
#         # self.scout_cam_label.img = self.scout_cam_image
#         # self.scout_cam_label.config(image = self.scout_cam_label.img)
#
#         # os.chdir('..')
#         self.datalist = DataList("download (3)")
#         print(os.getcwd())
#         self.datalist.extract_files("download (3)")
#         self.datalist.get_fixed_filename()
#         self.datalist.load_scout_healths()
#         self.datalist.load_scout_interactions()
#         self.datalist.load_scout_summaries()
#
#         # os.chdir('download (3)')
#         # print(os.getcwd())
#         print(os.listdir('.')[0])
#         self.scout_cam_image = Image.open(os.listdir('.')[0])
#         self.scout_cam_image.putalpha(128)  # Half alpha; alpha argument must be an int
#         self.scout_cam_image.save("./scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3.gif", "GIF")
#         # self.scout_cam_image = self.scout_cam_image.convert('RGBA')
#         # image_data = self.scout_cam_image.getdata()
#         # new_image_data = []
#         # new_image_data.append((0, 0, 0, 255))
#         # for item in image_data:
#         #     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         #         new_image_data.append((255, 255, 255, 100))
#         #     else:
#         #         new_image_data.append(item)
#         # self.scout_cam_image.putdata(new_image_data)
#         # self.scout_cam_image.save("./scout-1f31a16e-7096-4a98-bf8b-8a298deeb7d3.gif", "GIF")
#         #
#         # # self.scout_cam_image = self.scout_cam_image.resize((800, 250), Image.ANTIALIAS)
#         # self.scout_cam_image.paste(self.scout_cam_image, (0, 0), self.scout_cam_image)
#         self.scout_cam_canvas = Canvas(self.presentation_frame)
#         self.scout_cam_canvas.config(width = 640, height = 360, highlightthickness = 0)
#         print(self.scout_cam_canvas.config())
#         self.scout_cam_canvas.image = PIL.ImageTk.PhotoImage(self.scout_cam_image)
#         self.scout_cam_canvas.create_image(0, 0, image=self.scout_cam_canvas.image, anchor='nw', tags="IMG")
#         self.scout_cam_canvas.grid(row = 0, column = 0, rowspan = 20, columnspan = 20, stick = 'nsew')
#         # img = Image.open("flower.png")
#         self.scout_cam_canvas.bind("<Configure>", self.resize)
#
#         # def RBGAImage(path):
#         #     return Image.open(path).convert("RGBA")
#         #
#         # face = RBGAImage("faces/face.gif")
#         # eyes = RBGAImage("faces/eyes1.png")
#         #
#         # face.paste(eyes, (0, 0), eyes)
#         #
#         # facepic = ImageTk.PhotoImage(face)
#         #
#         # label1 = Label(image=facepic)
#         # label1.grid(row=0, column=0)
#
#         self.rect = self.scout_cam_canvas.create_rectangle(200, 250, 400, 400)
#         self.scout_cam_canvas.itemconfigure(self.rect, fill = 'yellow')
#
#         ttk.Label(self.presentation_frame, text = "Visitors: ").grid(row = 21, column = 2, columnspan = 2, stick = 'w')
#
#         # self.test_canvas = Canvas(self.presentation_frame, background = 'red', highlightthickness = 0)
#         # self.test_canvas.attributes('-alpha', 0.3)
#         # self.test_label.lift()
#         # self.test_canvas.grid(row = 2, column = 3, stick = 'nsew')
#         # self.scout_cam_canvas.create_rectangle()
#
#         # if table_association == "VisitTimeBuckets" and any(char.isdigit() for char in scout_summaries_component):
#         #     if visit_time_buckets_index_2 < 20:
#         #         visit_time_buckets_index_1.append(scout_summaries_component)
#         #         visit_time_buckets_index_2 += 1
#         #     else:
#         #         scout_summaries_instance.visit_time_buckets.append(visit_time_buckets_index_1)
#         #         visit_time_buckets_index_1 = []
#         #         visit_time_buckets_index_1.append(scout_summaries_component)
#         #         visit_time_buckets_index_2 = 1
#         # elif len(scout_summaries_instance.visit_time_buckets) == 19:
#         #     scout_summaries_instance.visit_time_buckets.append(visit_time_buckets_index_1)
#
#         self.presentation_frame.rowconfigure('all', weight = 1)
#         self.presentation_frame.columnconfigure('all', weight = 1)
#
#         year = StringVar()
#         self.year_combobox = ttk.Combobox(self.selection_frame, textvariable = year)
#         self.year_combobox.config(values = YEARS)
#         self.year_combobox.grid(row = 0, column = 1)
#
#         month = StringVar()
#         self.month_combobox = ttk.Combobox(self.selection_frame, textvariable = month)
#         self.month_combobox.config(values = MONTHS)
#         self.month_combobox.grid(row = 1, column = 1)
#
#         day = StringVar()
#         self.day_combobox = ttk.Combobox(self.selection_frame, textvariable = day)
#         self.day_combobox.config(values = DAYS)
#         self.day_combobox.grid(row = 2, column = 1)
#
#         hour = StringVar()
#         self.hour_combobox = ttk.Combobox(self.selection_frame, textvariable = hour)
#         self.hour_combobox.config(values = HOURS)
#         self.hour_combobox.grid(row = 3, column = 1)
#
#         # rescale all the objects tagged with the "all" tag
#         # self.scale("all", 0, 0)
