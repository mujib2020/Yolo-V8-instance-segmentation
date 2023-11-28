# -*- coding: utf-8 -*-
"""
Mujib Chowdhury
November 2023
"""
# load a pretrained model (recommended for training)

from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')  

model.train(data='config.yaml', epochs=100, imgsz=640)

