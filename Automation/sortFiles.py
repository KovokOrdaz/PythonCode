from distutils import extension
from pickletools import optimize
from PIL import Image
import os

folder = "D:\Downloads/"
folderPicture = r"C:\Users/PhoebePC/Desktop/Holis/"
folderMusic = r"D:\Music/"

if __name__ == "__main__":
    for filename in os.listdir(folder):
        name, extension = os.path.splitext(folder + filename)

        if extension in [".jpg", ".png", ".jpeg"]:
            picture = Image.open(folder + filename)
            picture.save(folderPicture + "compresed_" + filename,
                         optimize=True, quality=60)
            os.remove(folder + filename)
            print(name + ":" + extension)

        if extension in [".mp3"]:
            os.rename(folder + filename, folderMusic + filename)
