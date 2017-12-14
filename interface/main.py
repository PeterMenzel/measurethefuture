
from tkinter import *
from tkinter import ttk
import os
import wx
import wx.grid as gridlib
# import Image, ImageTk
# from Pillow import ImageTk, Image
# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
from PIL import ImageTk, Image
import PIL
from PIL import Image
from datalist import DataList
from scout_summaries import ScoutSummaries


YEARS = ["2017", "2018", "2019", "2020"]
MONTHS = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"] # Depends on Month...
HOURS = ["9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM"]
DATA_FILES = []

class MeasureTheFutureApp(wx.Frame):

    def __init__(self, parent, title):
        super(MeasureTheFutureApp, self).__init__(parent, title=title)

        self.init_ui()
        self.Bind(wx.EVT_COMBOBOX, self.on_data_file_selection, self.data_files_combo)
        self.Bind(wx.EVT_BUTTON, self.on_directory_button, self.directory_button)
        # self.Bind(wx.EVT_SIZE, self.on_size_change)
        self.Centre()
        self.Show()
        self.Maximize(True)

    def init_ui(self):

        wx.InitAllImageHandlers()
        self.directory_path = os.getcwd()

        self.get_data_files()

        self.main_panel = wx.Panel(self)
        self.main_panel_grid = wx.BoxSizer(wx.HORIZONTAL)

        self.selection_panel = wx.Panel(self.main_panel)
        self.selection_box = wx.BoxSizer(wx.VERTICAL)
        self.presentation_panel = wx.Panel(self.main_panel)
        self.presentation_box = wx.BoxSizer(wx.VERTICAL)

        self.selection_grid = wx.FlexGridSizer(5, 2, 10, 20)

        self.year = wx.StaticText(self.selection_panel, label="Year:")
        self.month = wx.StaticText(self.selection_panel, label="Month:")
        self.day = wx.StaticText(self.selection_panel, label="Day:")
        self.hour = wx.StaticText(self.selection_panel, label="Hour:")
        self.data_files = wx.StaticText(self.selection_panel, label="Data Files: ")
        self.directory_prompt = wx.StaticText(self.selection_panel, label="Choose a Directory: ")

        self.year_combo = wx.ComboBox(self.selection_panel, choices=YEARS, style=wx.CB_READONLY)
        self.month_combo = wx.ComboBox(self.selection_panel, choices=MONTHS, style=wx.CB_READONLY)
        self.day_combo = wx.ComboBox(self.selection_panel, choices=DAYS, style=wx.CB_READONLY)
        self.hour_combo = wx.ComboBox(self.selection_panel, choices=HOURS, style=wx.CB_READONLY)
        self.data_files_combo = wx.ComboBox(self.selection_panel, choices=DATA_FILES, style=wx.CB_READONLY)
        self.directory_button = wx.Button(self.selection_panel, label="open")

        self.selection_grid.AddMany([(self.data_files), (self.data_files_combo, 1, wx.EXPAND), (self.year),
                                     (self.year_combo, 1, wx.EXPAND), (self.month), (self.month_combo, 1, wx.EXPAND),
                                     (self.day), (self.day_combo, 1, wx.EXPAND), (self.hour),
                                     (self.hour_combo, 1, wx.EXPAND)])

        self.selection_box.Add(self.selection_grid, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.directory_box = wx.BoxSizer(wx.HORIZONTAL)
        self.directory_box.Add(self.directory_prompt, flag=wx.ALIGN_LEFT)
        self.directory_box.Add(self.directory_button, flag=wx.RIGHT|wx.BOTTOM, border=10)
        self.selection_box.Add(self.directory_box, flag=wx.ALIGN_BOTTOM|wx.BOTTOM|wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        # self.on_data_file_selection()

        # self.get_data_file_selection()
        #
        # self.load_datalist()
        #
        # self.load_scout_image()
        #
        # self.get_heat_map()

        # self.set_visitor_label()

        # self.get_visitor_count()





        self.selection_panel.SetSizer(self.selection_box)
        self.presentation_panel.SetSizer(self.presentation_box)

        self.main_panel_grid.Add(self.selection_panel, 0)
        self.main_panel_grid.Add(self.presentation_panel, 1, flag=wx.ALL | wx.EXPAND)
        self.main_panel.SetSizer(self.main_panel_grid)

        self.set_main_size()

    def set_presentation_box_sizer(self):
        self.presentation_box.Add(self.scout_image_panel, 0)
        self.presentation_box.Add(self.visitor_count_marker, 1, flag=wx.BOTTOM | wx.EXPAND | wx.ALIGN_BOTTOM)
        self.Layout()

    def set_main_size(self):
        # self.best_size_x = self.selection_panel.BestSize[0] + self.presentation_panel.BestSize[0]
        # self.best_size_y = self.presentation_panel.BestSize[1] + self.visitor_count_marker.BestSize[1]
        # self.SetSize(self.best_size_x, self.best_size_y)
        self.SetMinSize((self.Size))

    def get_heat_map(self):
        self.heat_map = gridlib.Grid(self.scout_image_control)
        self.heat_map.CreateGrid(20, 20)
        self.heat_map.EnableGridLines(False)
        self.heat_map.EnableEditing(False)
        self.heat_map.DisableDragRowSize()
        self.heat_map.DisableDragColSize()
        self.heat_map.HideRowLabels()
        self.heat_map.HideColLabels()
        print(self.heat_map.GetDefaultCellBackgroundColour())
        # print(self.heat_map.Alpha())
        # self.heat_map.SetDefaultCellBackgroundColour(0, 0, 0, 0)
        # self.heat_map.DC
        # self.heat_map.SetForegroundColour(0, 0, 0, 0)
        self.test = wx.GCDC()
        self.heat_map.SetSize(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        self.heat_map.SetDefaultRowSize(self.scout_image_dimensions[1] / 20, True)
        self.heat_map.SetDefaultColSize(self.scout_image_dimensions[0] / 20, True)
        self.scout_image_control_box.Add(self.heat_map, 1, flag=wx.ALL | wx.EXPAND)
        max_i = []
        for i in list(range(20)):
            max_i.append(max(self.datalist.scout_summaries.visit_time_buckets[i]))
        self.max_visit_time_bucket = max(max_i)
        self.max_visit_time_bucket /= 2
        for i in list(range(20)):
            for j in list(range(20)):
                time_bucket = self.datalist.scout_summaries.visit_time_buckets[i][j]
                if time_bucket > self.max_visit_time_bucket:
                    value = time_bucket - self.max_visit_time_bucket
                    colour = (int(255 * (value / self.max_visit_time_bucket)), 0, 0, int(255 * 0.5))
                else:
                    value = self.max_visit_time_bucket - time_bucket
                    colour= (0, 0, int(255 * (value / self.max_visit_time_bucket)), int(255 * 0.5))
                self.heat_map.SetCellBackgroundColour(i, j, (colour))

    def load_scout_image(self):
        os.chdir(self.file_selection)
        self.scout_image_panel = wx.Panel(self.presentation_panel)
        image_dimension_x = self.GetSize()[0] - self.selection_panel.GetSize()[0]
        image_dimension_y = self.GetSize()[1] - 20
        if image_dimension_x / image_dimension_y >= 16 / 9:
            self.scout_image_dimensions = ((image_dimension_y / 9) * 16) - 10, image_dimension_y - 10
        else:
            self.scout_image_dimensions = image_dimension_x - 10, ((image_dimension_x / 16) * 9) - 10
        self.scout_image_panel.SetSize(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        # self.scout_image_dimensions = self.scout_image_panel.GetSize()
        # os.system("magick convert {0}.jpg {0}.png".format(self.datalist.image_name))
        # im = Image.open("Ba_b_do8mag_c6_big.png")
        self.scout_image = Image.open("{}.jpg".format(self.datalist.image_name))
        self.scout_image = self.scout_image.convert('RGBA')
        self.scout_image.save("{}.png".format(self.datalist.image_name))
        self.scout_image = wx.Image("{}.png".format(self.datalist.image_name), wx.BITMAP_TYPE_ANY)
        self.scout_image.Rescale(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        print(self.scout_image.HasAlpha())
        self.scout_image.InitAlpha()
        print(self.scout_image.GetAlpha())
        self.scout_image_control = wx.StaticBitmap(self.scout_image_panel, wx.ID_ANY, wx.Bitmap(self.scout_image))
        self.scout_image_control.SetBitmap(wx.Bitmap(self.scout_image))
        self.scout_image_control_box = wx.BoxSizer(wx.VERTICAL)
        os.chdir('..')
        self.scout_image_control.SetSizer(self.scout_image_control_box)
        # print(self.scout_image.InitAlpha())
        print(self.scout_image.HasAlpha())
        # self.scout_image_control.
        # print(self.scout_image.GetAlpha())
        # self.scout_image.SetAlpha(127)

    def load_datalist(self):
        self.datalist = DataList(self.file_selection)
        self.datalist.extract_files(self.file_selection)
        # self.datalist.get_fixed_filename()
        self.datalist.get_image_name()
        self.datalist.load_scout_healths()
        self.datalist.load_scout_interactions()
        self.datalist.load_scout_summaries()
        os.chdir('..')

    def get_data_file_selection(self):
        self.file_selection = self.data_files_combo.GetValue()

    def get_data_files(self):
        for file in os.listdir("."):
            if file.endswith(".zip"):
                DATA_FILES.append(file[:file.find('.')])

    def get_visitor_count(self):
        self.vistor_count = self.datalist.scout_summaries.visitor_count
        self.visitor_count_marker.SetLabel("Visitors: {}".format(
            self.vistor_count))

    def set_visitor_label(self):
        self.visitor_count_marker = wx.StaticText(self.presentation_panel, label="Visitors: ")
        self.visitor_count_font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.visitor_count_marker.SetFont(self.visitor_count_font)

    def on_data_file_selection(self, event):
        # self.heat_map.Destroy()
        # self.scout_image.Destroy()
        # self.scout_image_control.Destroy()
        os.chdir(self.directory_path)
        self.get_data_file_selection()
        self.load_datalist()
        self.load_scout_image()
        self.get_heat_map()
        self.set_visitor_label()
        self.set_presentation_box_sizer()
        self.get_visitor_count()
        self.Layout()

    def on_directory_button(self, event):
        self.directory = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE
                           # | wx.DD_DIR_MUST_EXIST
                           # | wx.DD_CHANGE_DIR
                           )
        if self.directory.ShowModal() == wx.ID_OK:
            print("You chose %s" % self.directory.GetPath())
        self.directory.Destroy()
        self.directory_path = self.directory.GetPath()

    def on_size_change(self, event):
        event.Skip()
        image_dimension_x = self.GetSize()[0] - self.selection_panel.BestSize[0]
        image_dimension_y = self.GetSize()[1] - self.visitor_count_marker.BestSize[1]
        if image_dimension_x / image_dimension_y >= 16 / 9:
            self.scout_image_dimensions = ((image_dimension_y / 9) * 16), image_dimension_y
        else:
            self.scout_image_dimensions = image_dimension_x, ((image_dimension_x / 16) * 9)
        self.presentation_panel.SetSize(self.scout_image_dimensions[0], self.GetSize()[1])
        self.scout_image_panel.SetSize(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        self.scout_image.Rescale(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        self.scout_image_control.SetBitmap(wx.Bitmap(self.scout_image))
        self.heat_map.SetDefaultRowSize(self.scout_image_dimensions[1] / 20, True)
        self.heat_map.SetDefaultColSize(self.scout_image_dimensions[0] / 20, True)
        self.scout_image_control.SetSize(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        self.presentation_panel.SetMinSize(self.presentation_panel.GetSize())
        self.scout_image_panel.SetMinSize(self.scout_image_panel.GetSize())
        # self.scout_image.Scale(self.scout_image.GetSize()[0], self.scout_image.GetSize()[1])
        # self.scout_image_control.SetMinSize(self.scout_image_control.GetSize())
        # self.scout_image.Rescale(self.scout_image_dimensions[0], self.scout_image_dimensions[1])
        self.Layout()



if __name__ == '__main__':
    app = wx.App()
    MeasureTheFutureApp(None, title='Measure The Future - Townsville CityLibraries')
    app.MainLoop()
