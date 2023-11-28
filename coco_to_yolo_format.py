# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 08:47:38 2023

@author: Mujib 

We download the coco format from CVAT, then convert them into yolo format using this script


"""


# COCO Dataset Format to YOLO Format
from ultralytics.data.converter import convert_coco

coco_path = r"C:\All_data_from_Box\Miscellaneous_copy\Data_Projects\Computer_Vision_And_DL\Yolo_V8\images_wood120\job_427658-2023_11_24_22_01_42-coco 1.0\annotations"
convert_coco(labels_dir=coco_path, use_segments=True)






# #  auto anotation, we haven't use it here though
# from ultralytics.data.annotator import auto_annotate

# auto_annotate(data="images_wood120/images", det_model="yolov8x.pt", sam_model='sam_b.pt')