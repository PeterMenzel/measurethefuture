
import zipfile
import json
import os
import shutil
# import Image
# import Image, ImageTk
# from Pillow import ImageTk, Image
# from PIL import ImageTk, Image


class DataList:

    def __init__(self, filename, scout_healths=[], scout_interactions=[], scout_summaries=[], scouts=[]):
        self.filename = filename
        self.zip_filename = "{}.zip".format(filename)
        self.scout_healths = scout_healths
        self.scout_interactions = scout_interactions
        self.scout_summaries = scout_summaries
        self.scouts = scouts

    def extract_data(self, filename):
        with zipfile.ZipFile(self.zip_filename, 'r') as data_folder:
            files = data_folder.namelist()
            data_folder.extractall()
        print(files)
        print("Current directory is", os.getcwd())
        os.chdir(filename)
        print("Current directory is", os.getcwd())
        # print a list of all files (test)
        print(os.listdir('.'))
        return files

    def get_fixed_filename(self):
        """Return a 'fixed' version of filename."""
        # im = Image.open(os.listdir('.')[0])
        # im.save('scout_image.gif')
        for file in os.listdir('.'):
            new_name = file.replace(".json", ".csv") #.replace(".jpg", ".gif")
            os.rename(file, new_name)
            print(new_name)
        print(os.listdir('.'))

    def load_scout_healths(self):
        in_scout_healths_file = open("scout_healths.csv")
        in_scout_healths = in_scout_healths_file.readlines()
        for i in range(len(in_scout_healths)):
            scout_healths_component = in_scout_healths[i].split(",")
            # if scout_healths[3] == "y\n":
            #     is_required = True
            # else:
            #     is_required = False
            # self.songs.append(Song(song[0], song[1], int(song[2]), is_required))  # create list of lists
            print(scout_healths_component)
        in_scout_healths_file.close()
