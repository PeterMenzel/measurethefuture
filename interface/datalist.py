
import zipfile
import json
import os
import shutil

class DataList:

    def load_data(self):
        pass


def main():
    with zipfile.ZipFile('11_29_0830.zip', 'r') as f:
        names = f.namelist()
        f.extractall()
        # print(f.extractall())
        # d = open('scouts.txt')
    print(names)
    # f = open('scouts.json', 'r')
    # print(f)
    # f.close()
    print("Current directory is", os.getcwd())
    os.chdir('11_29_0830')
    print("Current directory is", os.getcwd())
    # print a list of all files (test)
    print(os.listdir('.'))
    for filename in os.listdir('.'):
        # ignore directories, just process files
        # if not os.path.isdir(filename):
        #     new_name = get_fixed_filename(filename)
        #     print(new_name)
        new_name = get_fixed_filename(filename)
        print(new_name)
        os.rename(filename, new_name)
    print(os.listdir('.'))

def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    # filename = filename.replace(".json", ".txt")
    # new_name = ""
    new_name = filename.replace(".json", ".csv")
    return new_name


# data = zipfile.ZipFile('11_29_0830.zip')
# datalist = data.read('scout_healths.txt')
# data.close()
# print(datalist)
#
# with open('scout_healths.json') as json_data:
#     d = json.load(json_data)
#     print(d)
#
# data.close()

# print(d)
# d.close()
# with open(f['11_29_0830/scouts.json']) as json_data:
#     d = json.load(json_data)
#     print(d)
# d = open('scouts.txt')
# data = d.read()
# print(data)
# d.close()
main()