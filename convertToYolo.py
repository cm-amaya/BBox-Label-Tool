# -*- coding: utf-8 -*-
"""
This script is to convert the txt annotation files to appropriate format needed by YOLO 

Based on previous work by: Guanghan Ning (gnxr9@mail.missouri.edu)
"""

import os
from os import walk, getcwd
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('--ndir', type=int,default=1, help='Number of the directory for conversion')
args = parser.parse_args()

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
    
""" Configure Paths"""   
folder_num = args.ndir
mypath = "Labels/{}/".format(str(folder_num).zfill(3))
outpath = "Labels/{}-YOLO/".format(str(folder_num).zfill(3))
imgdir = "Images/{}/".format(str(folder_num).zfill(3))

if not os.path.exists(outpath):
    os.mkdir(outpath)

wd = getcwd()
list_file = open('%s/training_list.txt'%(wd), 'w')

""" Get input text file list """
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
print(txt_name_list)

""" Process """
for txt_name in txt_name_list:
    # txt_file =  open("Labels/stop_sign/001.txt", "r")
    
    """ Open input text files """
    txt_path = mypath + txt_name
    print("Input:" + txt_path)
    txt_file = open(txt_path, "r")
    lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
    
    """ Open output text files """
    txt_outpath = outpath + txt_name
    print("Output:" + txt_outpath)
    txt_outfile = open(txt_outpath, "w")
    
    
    """ Convert the data to YOLO format """
    ct = 0
    for line in lines:
        if(len(line) >= 3):
            ct = ct + 1
            print(line + "\n")
            elems = line.split(' ')
            print(elems)
            xmin = elems[0]
            xmax = elems[2]
            ymin = elems[1]
            ymax = elems[3]
            classname = elems[4]
            namec,splitc=classname.split("-")
            #
            imgpath = str('%s/%s.png'%(imgdir, os.path.splitext(txt_name)[0]))
            if not os.path.exists(imgpath):
                imgpath = str('%s/%s.jpg'%(imgdir, os.path.splitext(txt_name)[0]))
            if not os.path.exists(imgpath):
                continue
            #t = magic.from_file(img_path)
            #wh= re.search('(\d+) x (\d+)', t).groups()
            im=Image.open(imgpath)
            im.save(str('%s/%s.jpg'%(outpath, os.path.splitext(txt_name)[0])))
            w= int(im.size[0])
            h= int(im.size[1])
            #w = int(xmax) - int(xmin)
            #h = int(ymax) - int(ymin)
            # print(xmin)
            print(w, h)
            b = (float(xmin), float(xmax), float(ymin), float(ymax))
            bb = convert((w,h), b)
            print(bb)
            txt_outfile.write(str(splitc) + " " + " ".join([str(a) for a in bb]) + '\n')

    """ Save those images with bb into list"""
    if(ct != 0):
        list_file.write('%s/images/%s.png\n'%(wd,os.path.splitext(txt_name)[0]))
                
list_file.close()       
