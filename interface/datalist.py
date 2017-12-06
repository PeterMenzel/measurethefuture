from scout_healths import ScoutHealths

from scout_summaries import ScoutSummaries
import zipfile
import json
import os
import shutil
# import Image
# import Image, ImageTk
# from Pillow import ImageTk, Image
# from PIL import ImageTk, Image
# SCOUT_HEALTHS_ATTRIBUTES = ["ScoutUUID", "CPU", "Memory", "TotalMemory", "Storage", "CreatedAt"]


class DataList:

    def __init__(self, filename, scout_healths=[], scout_interactions=[], scout_summaries=[], scouts=[]):
        self.filename = filename
        self.zip_filename = "{}.zip".format(filename)
        self.scout_healths = scout_healths
        self.scout_interactions = scout_interactions
        self.scout_summaries = scout_summaries
        self.scouts = scouts

    def extract_files(self, filename):
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
        scout_healths_instance = ScoutHealths()
        in_scout_healths_file = open("scout_healths.csv")
        in_scout_healths = in_scout_healths_file.readlines()
        for i in range(len(in_scout_healths)):
            scout_healths_component = in_scout_healths[i].split(",")[0][2:]
            # print(scout_healths_component)
            if scout_healths_component.startswith("ScoutUUID", 1):
                scout_healths_instance.scout_id.append(scout_healths_component[scout_healths_component.find(':') + 3:-1])
                # scout_healths_instance.scout_id = "test"
                print(scout_healths_instance.scout_id)
            elif "CPU" in scout_healths_component:
                scout_healths_instance.cpu.append(scout_healths_component[scout_healths_component.find(':') + 2:])
                # scout_healths_instance.scout_id = "test"
                print(scout_healths_instance.cpu)
            elif "CreatedAt" in scout_healths_component:
                scout_healths_instance.created_at.append(scout_healths_component[scout_healths_component.find(':') + 3:-2])
                # scout_healths_instance.scout_id = "test"
                print(scout_healths_instance.created_at)
            elif "TotalMemory" in scout_healths_component:
                scout_healths_instance.total_memory.append(scout_healths_component[scout_healths_component.find(':') + 2:])
                # scout_healths_instance.scout_id = "test"
                print(scout_healths_instance.total_memory)
            elif "Storage" in scout_healths_component:
                scout_healths_instance.storage.append(scout_healths_component[scout_healths_component.find(':') + 2:])
                # scout_healths_instance.scout_id = "test"
                print(scout_healths_instance.storage)
            elif "Memory" in scout_healths_component:
                scout_healths_instance.memory.append(scout_healths_component[scout_healths_component.find(':') + 2:])
                # scout_healths_instance.scout_id = "test"
                print(scout_healths_instance.memory)

        print(in_scout_healths)
        print(in_scout_healths[2])
        in_scout_healths_file.close()

    def load_scout_interactions(self):
        in_scout_interactions_file = open("scout_interactions.csv")
        in_scout_interactions = in_scout_interactions_file.readlines()
        for i in range(len(in_scout_interactions)):
            scout_interactions_component = in_scout_interactions[i].split(",")

        print(in_scout_interactions)
        in_scout_interactions_file.close()

    def load_scout_summaries(self):
        scout_summaries_instance = ScoutSummaries()
        in_scout_summaries_file = open("scout_summaries.csv")
        in_scout_summaries = in_scout_summaries_file.readlines()
        # for i in range(len(in_scout_summaries)):
        #     scout_summaries_component = in_scout_summaries[i].split(",")[0][2:]
        #     # print(scout_healths_component)
        #     if scout_summaries_component.startswith("ScoutUUID", 1):
        #         scout_summaries_instance.scout_id.append(scout_summaries_component[scout_summaries_component.find(':') + 3:-1])
        #         # scout_healths_instance.scout_id = "test"
        #         print(scout_summaries_instance.scout_id)
        #     elif "CPU" in scout_summaries_component:
        #         scout_summaries_instance.cpu.append(scout_summaries_component[scout_summaries_component.find(':') + 2:])
        #         # scout_healths_instance.scout_id = "test"
        #         print(scout_summaries_instance.cpu)
        #     elif "CreatedAt" in scout_summaries_component:
        #         scout_summaries_instance.created_at.append(scout_summaries_component[scout_summaries_component.find(':') + 3:-2])
        #         # scout_healths_instance.scout_id = "test"
        #         print(scout_summaries_instance.created_at)
        #     elif "TotalMemory" in scout_summaries_component:
        #         scout_summaries_instance.total_memory.append(scout_summaries_component[scout_summaries_component.find(':') + 2:])
        #         # scout_healths_instance.scout_id = "test"
        #         print(scout_summaries_instance.total_memory)
        #     elif "Storage" in scout_summaries_component:
        #         scout_summaries_instance.storage.append(scout_summaries_component[scout_summaries_component.find(':') + 2:])
        #         # scout_healths_instance.scout_id = "test"
        #         print(scout_summaries_instance.storage)
        #     elif "Memory" in scout_summaries_component:
        #         scout_summaries_instance.memory.append(scout_summaries_component[scout_summaries_component.find(':') + 2:])
        #         # scout_healths_instance.scout_id = "test"
        #         print(scout_summaries_instance.memory)
        print(in_scout_summaries)
        in_scout_summaries_file.close()
