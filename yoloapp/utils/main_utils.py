import os 
import sys
import yaml
import os.path
import base64


def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + fileName,'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())        