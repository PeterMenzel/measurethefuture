

from datalist import DataList
import os

data1 = DataList("11_29_0830")
data1.extract_data("11_29_0830")
data1.get_fixed_filename()
data1.load_scout_healths()

os.chdir('..')
print(os.getcwd())
data2 = DataList("download (3)")
data2.extract_data("download (3)")
data2.get_fixed_filename()

data2.load_scout_healths()

