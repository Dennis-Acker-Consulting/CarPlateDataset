#importing the required package
from PIL import Image
import os


directories = ['train_dir/annotations', 'val_dir/annotations']

for dir in directories:
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for file in filenames: 
            path = dir + "/" + file
            searchPhrase = '.png'
            replacePhrase = '.jpg'

            f = open(path, "r+")
            data = f.read().replace(searchPhrase, replacePhrase)
            f.truncate(0)
            f.seek(0)
            f.write(data)
            f.close()