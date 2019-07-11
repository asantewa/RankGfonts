#pull all html in a root directory

import os

rootdir = os.getcwd()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".html"):
            print (filepath)
