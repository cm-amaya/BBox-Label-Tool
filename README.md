# BBox-Label-Tool v2

A simple tool for labeling object bounding boxes in images with Python

## Data Organization
```
LabelTool
|
|--main.py # source code for the tool
|
|--convertToYolo.py #  code to turn labels to YOLO format
|
|--classes.txt # list of classes
|
|--Images/ # directroy containing the images to be labeled
|
|--Labels/ # directory for the labeling results
|
|--Examples/ # direcotry for the example bboxes
```

## Environment

    python 3.7
    python PIL (Pillow)

## Run
```
$ python main.py
```
## Usage

1. The current tool requires that the images to be labeled reside in /Images/001, /Images/002, etc. Additionaly, modify the class list in classes.txt.

2. Input a folder number (e.g, 1, 2, 5...), and click Load. The images in the folder, along with a few example results will be loaded.

3. To create a new bounding box, left-click to select the first vertex. Moving the mouse to draw a rectangle, and left-click again to select the second vertex.
  * To cancel the bounding box while drawing, just press Esc.
  * To delete a existing bounding box, select it from the listbox, and click Delete.
  * To delete all existing bounding boxes in the image, simply click ClearAll or right click with the mouse.

4. After finishing one image, click Next to advance. Likewise, click Prev to reverse. Or, input an image id and click Go to navigate to the speficied image. You can also use the mouse wheel for navigation

5. Be sure to click Next after finishing a image, or the result won't be saved.
