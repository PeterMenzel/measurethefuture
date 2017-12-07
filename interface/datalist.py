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
        table_association = None
        visit_time_buckets_index_1 = []
        visit_time_buckets_index_2 = 0
        visitor_buckets_index_1 = []
        visitor_buckets_index_2 = 0
        # print(len(in_scout_summaries))
        for i in range(len(in_scout_summaries)):
            scout_summaries_component = in_scout_summaries[i].split(",")[0][2:].strip(' ').strip('\n')
            # scout_summaries_component = in_scout_summaries[i].strip(' ').strip('\n')
            print(scout_summaries_component)
            if scout_summaries_component.startswith("ScoutUUID", 1):
                scout_summaries_instance.scout_id = scout_summaries_component[scout_summaries_component.find(':') + 3:-1]
                # scout_healths_instance.scout_id = "test"
                print(scout_summaries_instance.scout_id)
            elif "VisitorCount" in scout_summaries_component:
                scout_summaries_instance.visitor_count = scout_summaries_component[scout_summaries_component.find(':') + 2:]
                # scout_healths_instance.scout_id = "test"
                print(scout_summaries_instance.visitor_count)
            elif "VisitTimeBuckets" in scout_summaries_component or "VisitorBuckets" in scout_summaries_component:
                if scout_summaries_component.startswith("VisitTimeBuckets", 1):
                    table_association = "VisitTimeBuckets"
                elif scout_summaries_component.startswith("VisitorBuckets", 1):
                    table_association = "VisitorBuckets"
            elif table_association == "VisitTimeBuckets" and any(char.isdigit() for char in scout_summaries_component):
                if visit_time_buckets_index_2 < 20:
                    visit_time_buckets_index_1.append(scout_summaries_component)
                    visit_time_buckets_index_2 += 1
                else:
                    scout_summaries_instance.visit_time_buckets.append(visit_time_buckets_index_1)
                    visit_time_buckets_index_1 = []
                    visit_time_buckets_index_1.append(scout_summaries_component)
                    visit_time_buckets_index_2 = 1
            elif len(scout_summaries_instance.visit_time_buckets) == 19:
                scout_summaries_instance.visit_time_buckets.append(visit_time_buckets_index_1)
            elif table_association == "VisitorBuckets" and any(char.isdigit() for char in scout_summaries_component):
                if visitor_buckets_index_2 < 20:
                    # scout_summaries_instance.visitor_buckets[visitor_buckets_index_1][
                    #     visitor_buckets_index_2] = scout_summaries_component
                    visitor_buckets_index_1.append(scout_summaries_component)
                    visitor_buckets_index_2 += 1
                else:
                    # scout_summaries_instance.visitor_buckets[visitor_buckets_index_1][
                    #     visitor_buckets_index_2] = scout_summaries_component
                    scout_summaries_instance.visitor_buckets.append(visitor_buckets_index_1)
                    visitor_buckets_index_1 = []
                    visitor_buckets_index_1.append(scout_summaries_component)
                    visitor_buckets_index_2 = 1
            elif len(scout_summaries_instance.visitor_buckets) == 19:
                scout_summaries_instance.visitor_buckets.append(visitor_buckets_index_1)
                # scout_summaries_instance.visit_time_buckets.append(scout_summaries_component[scout_summaries_component.find(':') + 3:-2])
                # if scout_summaries_component.isdigit():
                #     pass
                # print(scout_summaries_instance.visit_time_buckets)
            # if scout_summaries_component.startswith("ScoutUUID", 1):
            #     scout_summaries_instance.scout_id = scout_summaries_component[scout_summaries_component.find(':') + 3:-1]
            #     # scout_healths_instance.scout_id = "test"
            #     print(scout_summaries_instance.scout_id)
            # elif "VisitorCount" in scout_summaries_component:
            #     scout_summaries_instance.visitor_count = scout_summaries_component[scout_summaries_component.find(':') + 2:]
            #     # scout_healths_instance.scout_id = "test"
            #     print(scout_summaries_instance.visitor_count)
            # elif "VisitTimeBuckets" in scout_summaries_component:
            #     # scout_summaries_instance.visit_time_buckets.append(scout_summaries_component[scout_summaries_component.find(':') + 3:-2])
            #     if scout_summaries_component.isdigit():
            #         pass
            #     print(scout_summaries_instance.visit_time_buckets)
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
        print(scout_summaries_instance.visit_time_buckets)
        print(len(scout_summaries_instance.visit_time_buckets))
        print(len(scout_summaries_instance.visit_time_buckets[18]))
        print(scout_summaries_instance.visitor_buckets)
        print(in_scout_summaries)
        # print(in_scout_summaries.split(",")[0][2:])
        in_scout_summaries_file.close()
