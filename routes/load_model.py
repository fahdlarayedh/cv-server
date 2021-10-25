# -*- coding: utf-8 -*-

from io import StringIO
import zipfile
import pathlib
import base64
import io
import numpy as np
import os
import sys
import json
import tarfile
import pyzbar.pyzbar as pz
import pytesseract
import cv2

#import easyocr
#from pdf2image import convert_from_path
#from matplotlib import pyplot as plt
#import numpy as np
#from io import BytesIO
#import requests
#try:
# from PIL import Image
#except ImportError:
# import Image
#import qrtools

detectionData = 'false'
test = 'my test'
evaxData = ''
qrCodeData = ''


def convert_to_image(imgstring):
  imgdata = base64.b64decode(imgstring)
  filename = 'public/images/image.jpg'  # I assume you have a way of picking unique filenames
  with open(filename, 'wb') as f:
    f.write(imgdata)
  im_rgb = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
  return im_rgb

def launch(evax_img):
  pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
  #img = cv2.imread('fahd.jpg')
  extract = pytesseract.image_to_string(evax_img)
  #print(extract)
  array=extract.split('\n')
  cleanResult=[]
  for res in array:
    if(len(res)>0):
      if ':' in res:
        metadata=res.split(':')
        if len(metadata)==3:
          tmpArray=[]
          tmpArray.append(metadata[0])
          x=metadata[1].split()
          if len(x) >5 :
            tmpArray.append(x[0]+" "+x[1]+" "+x[2])
            cleanResult.append(["recap",metadata[2]])
          else:
            if len(x)>3:
              cleanResult.append([x[1]+" "+x[3],metadata[2]])
            tmpArray.append(x[0])

          cleanResult.append(tmpArray)
        else:
          x=metadata[1].split()
          if  len(x)>5:
            cleanResult.append([metadata[0],x[0]])
          else:
            cleanResult.append(metadata)
  cleanResult[-1][0]=cleanResult[-1][0].replace('4','1')
  if 'N° dose' in cleanResult[-2][0]:
    cleanResult[-2][0]='N° lot dose 2'
  if 'recap' in cleanResult[-4][0]:
    cleanResult[-4][0]='Date de la vaccination dose 2'

  #print(cleanResult)
  #j=0
  #for cc in cleanResult:
      #print(cc[0],cc[1],j)
      #print(j)
      #j=j+1
      #for c in cc:
          #print(c)
  print('')

  xt = {
    "name": cleanResult[0][1],
    "idNumber": cleanResult[2][1],
    "lotVaccin1": cleanResult[11][1],
    "lotVaccin2": cleanResult[10][1],
    "dateOfBirth": cleanResult[3][1],
    "vaccinType": cleanResult[5][1],
    "vaccin1Date":cleanResult[9][1],
    "vaccin2Date":cleanResult[8][1],
    "vaccinationCenter1":cleanResult[6][1],
    "vaccinationCenter2":cleanResult[7][1],
    "nodeId":cleanResult[4][1]
  }

  x= {
    "name": "FAHD LARAYEDH",
    "idNumber": "07492285",
    "lotVaccin1": "025D21A",
    "lotVaccin2": "025D21A",
    "dateOfBirth": "1998-06-06",
    "vaccinType": "MODERNA",
    "vaccin1Date":"2021-08-15T14:00:00.000+0100",
    "vaccin2Date":"2021-09-11T12:30:00.000+0100",
    "vaccinationCenter1":"Lycée Menzah 6",
    "vaccinationCenter2":"Lycée Menzah 6",
    "nodeId":"ZiuChCvSCfaJR4SY5DvhAyZjweHLXotRNbXxjeAFqeD"
  }


  global evaxData
  evaxData = json.dumps(xt)

  code = pz.decode(evax_img)
  global qrCodeData
  qrCodeData = json.loads(code[0][0])

  return "done"




