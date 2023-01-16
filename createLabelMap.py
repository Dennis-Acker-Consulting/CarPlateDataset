#importing the required package
from PIL import Image
import os


directories = ['train_dir/annotations', 'val_dir/annotations']

labelmapPath = "label_map.pbtxt"
labelMap = open(labelmapPath, "w")
for dir in directories:
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for file in filenames: 
            path = dir + "/" + file
            print(path)
            f = open(path, "r+")
            data = f.read()
            print(data)
            break
