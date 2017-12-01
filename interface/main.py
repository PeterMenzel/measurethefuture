
from tkinter import *
from tkinter import ttk
YEARS = ["2017", "2018", "2019", "2020"]
MONTHS = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = ["1", "2", "3", "4", "5"]
HOURS = ["9AM", "10AM", "11AM", "12PM", "1PM", "2PM", "3PM", "4PM", "5PM", "6PM"]

class MeasureTheFutureApp:

    def __init__(self, master):

        master.title('Measure The Future - Townsville CityLibraries')

        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()
        self.selection_frame = ttk.Frame(master)
        self.selection_frame.pack()
        self.presentation_frame = ttk.Frame(master)
        self.presentation_frame.pack()

        self.year_label = ttk.Label(self.selection_frame, text = "Year:")
        self.year_label.grid(row = 0, column = 0)
        self.month_label = ttk.Label(self.selection_frame, text = "Month:")
        self.month_label.grid(row = 1, column = 0)
        self.day_label = ttk.Label(self.selection_frame, text = "Day:")
        self.day_label.grid(row = 2, column = 0)
        self.hour_label = ttk.Label(self.selection_frame, text = "Hour:")
        self.hour_label.grid(row = 3, column = 0)

        ttk.Label(self.presentation_frame, text = "Visitors: ")

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


def main():

    root = Tk()
    app = MeasureTheFutureApp(root)
    root.mainloop()

if __name__ == "__main__": main()