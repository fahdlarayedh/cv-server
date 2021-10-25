from io import StringIO
import zipfile
import cv2
import pathlib
import base64
import io
import numpy as np
import os
import sys
import json
import tarfile

detection = 'false'
test = 'my test'


def convert_to_image(imgstring):
  imgdata = base64.b64decode(imgstring)
  filename = 'public/images/image.jpg'  # I assume you have a way of picking unique filenames
  with open(filename, 'wb') as f:
    f.write(imgdata)
  im_rgb = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
  global detection
  detection = 'true'
  return im_rgb
