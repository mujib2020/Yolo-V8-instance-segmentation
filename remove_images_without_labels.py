# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:53:24 2023

@author: Mujib Chowdhury

- This script is to delete images that don't have labels. 
- During annotation on CVAT, I deleted some images. 
- After dowloading the labels from CVAT, I remove the corresponding images from the local as well
"""

import os


labels_path = r'C:\All_data_from_Box\Miscellaneous_copy\Data_Projects\Computer_Vision_And_DL\Yolo_V8\images_wood120\task_121_wood_surface_images-2023_11_24_22_39_02-segmentation mask 1.1\SegmentationClass'
images_path = 'images_wood120/train'

# Get the list of label and image files
labels = set(os.listdir(labels_path))
images = set(os.listdir(images_path))

# Find image files without a corresponding label file (The image file names without the extension match the label file names)
missing_labels = {image.split('.')[0] for image in images} - {label.split('.')[0] for label in labels}

# Now find the actual image file names that are missing labels
images_to_delete = {image for image in images if image.split('.')[0] in missing_labels}

# Delete the images that do not have corresponding label files
for image in images_to_delete:
    os.remove(os.path.join(images_path, image))

print(f'Deleted images: {images_to_delete}')
