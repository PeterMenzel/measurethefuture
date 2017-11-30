
import zipfile
import json
import os
import shutil


class DataList:

    def __init__(self, zip_filename):
        self.zip_filename = zip_filename

    def extract_data(self):
        with zipfile.ZipFile(self.zip_filename, 'r') as data_folder:
            files = data_folder.namelist()
            data_folder.extractall()
        print(files)
        print("Current directory is", os.getcwd())
        os.chdir('11_29_0830')
        print("Current directory is", os.getcwd())
        # print a list of all files (test)
        print(os.listdir('.'))
        return files

    def get_fixed_filename(self):
        """Return a 'fixed' version of filename."""
        for file in os.listdir('.'):
            new_name = file.replace(".json", ".csv").replace(".jpg", ".gif")
            os.rename(file, new_name)
            print(new_name)
        print(os.listdir('.'))

