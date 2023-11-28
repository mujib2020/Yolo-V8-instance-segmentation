# -*- coding: utf-8 -*-
"""
Mujib Chowdhury
November 2023
"""
# load a pretrained model (recommended for training)

from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')  

model.train(data='config.yaml', epochs=100, imgsz=640)

#====== Prediction ===========

# Predict using this line of code: ignore the error. 
!yolo task = segment mode = predict model = 'Results_202311/From_colab_20231125_train5-20231125T181127Z-001/train5/weights/best.pt' source = 'C:/All_data_from_Box/Miscellaneous_copy/Data_Projects/Computer_Vision_And_DL/Yolo_V8/images_wood120/data_final/images/test'
