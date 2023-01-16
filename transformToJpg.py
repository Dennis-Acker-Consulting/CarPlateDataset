#importing the required package
from PIL import Image
import os


directories = ['train_dir/images', 'val_dir/images']

for dir in directories:
    for (dirpath, dirnames, filenames) in os.walk(dir):
        for file in filenames: 
            if ('.png' in file):
                img_png = Image.open(dir + "/" + file)
                newImageName = file.replace(".png", ".jpg")
                print(newImageName)
                img_png = img_png.convert("RGB")
                img_png.save(dir + "/" + newImageName)
                os.remove(dir + "/" + file)
        # print(filenames)


# #open image in png format
# img_png = Image.open('C:\gfg\img.png')

# #The image object is used to save the image in jpg format
# img_png.save('C:\gfg\modified_img.jpg')


