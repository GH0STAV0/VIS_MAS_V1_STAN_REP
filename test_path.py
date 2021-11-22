import os

PATH = './last_bin'
if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print("File exists and is readable")
else:
    print("Either the file is missing or not readable")