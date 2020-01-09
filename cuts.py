# -*- coding: utf-8 -*-
"""
This script is to convert the txt annotation files to appropriate format needed by YOLO 

Based on previous work by: Guanghan Ning (gnxr9@mail.missouri.edu)
"""

import os
from os import walk, getcwd
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Crop boxes')
parser.add_argument('--ndir', type=int,default=1, help='Number of the directory for conversion')
args = parser.parse_args()


""" Configure Paths"""   
folder_num = args.ndir
folder_str = str(folder_num).zfill(3)
mypath = "Labels/{}/".format(folder_str)
outpath = "Cuts/{}/".format(folder_str)
imgdir = "Images/{}/".format(folder_str)

if not os.path.exists("Cuts"):
    os.mkdir("Cuts")
if not os.path.exists(outpath):
    os.mkdir(outpath)

wd = getcwd()

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    for filename in filenames:
        if '.txt' in filename:
            txt_name_list.append(filename)

""" Process """
for txt_name in txt_name_list:  
    ct = 0
    basename = os.path.splitext(txt_name)[0]
    
    for line in lines:
        if(len(line) >= 3):
            ct = ct + 1
            elems = line.split(' ')
            xmin = int(elems[0])
            xmax = int(elems[2])
            ymin = int(elems[1])
            ymax = int(elems[3])
            classname = elems[4]
            namec,splitc=classname.split("-")
            
            imgpath = str('%s/%s.png'%(imgdir, basename))
            if not os.path.exists(imgpath):
                imgpath = str('%s/%s.jpg'%(imgdir, basename))
            if not os.path.exists(imgpath):
                continue
            #t = magic.from_file(img_path)
            #wh= re.search('(\d+) x (\d+)', t).groups()
            im=Image.open(imgpath)
            w= int(im.size[0])
            h= int(im.size[1])
            
            crop = im.crop(xmin,ymin,xmax,ymax)
            crop_path = str('%s/%s-%i.jpg'%(outpath, basename,ct))
            crop.save(crop_path)
               
