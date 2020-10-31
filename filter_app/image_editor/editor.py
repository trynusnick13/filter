import ntpath
import numpy as np
import tkinter as tk
from copy import deepcopy
from tkinter import filedialog
from PIL import Image as Pillow


class ImageEditor:
    def __init__(self, command_history, filters):
        pass

    def load_image(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()           # asking a user for files path using built-in tkinter
        file_path_copy = deepcopy(file_path)                # copy for file name, in order to save original path intact
        image_dict = {}                                     # empty dictionary to store photos
        for i in range(len(file_path)):
            file_path_to_open = file_path[i]                # file path to one specific photo
            im = Pillow.open(file_path_to_open)             # opening photo using Pillow 8.0.1
            tail = ntpath.split(file_path_copy[i])          # getting file name from file path
            print(tail[1], im.format, im.mode, im.size)
            image_dict.update({tail[1]: np.asarray(im)})    # updating dictionary with a new photo

    def filtering(self):
        pass

