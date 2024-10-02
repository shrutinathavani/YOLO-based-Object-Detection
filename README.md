# YOLO Object Detection for Washing Machine Timers and Shafts 🕒🔍

## Introduction
Object detection is a crucial task in computer vision used across various applications, including surveillance, autonomous vehicles, and industrial automation. This repository discusses the implementation of the YOLO (You Only Look Once) algorithm specifically tailored for detecting washing machine timers and shafts. YOLO is renowned for its real-time object detection capabilities, speed, and accuracy.

## YOLO Algorithm Overview
The YOLO algorithm, standing for "You Only Look Once," is a deep learning-based object detection system that revolutionized real-time object detection. Key characteristics of YOLO include:
- **Single Pass**: YOLO divides the input image into a grid, enabling simultaneous predictions of bounding boxes and class probabilities for all objects in a single pass.
- **Anchor Boxes**: It uses anchor boxes to predict multiple bounding boxes for each grid cell, efficiently capturing objects of different shapes and sizes.
- **Class Prediction**: YOLO predicts class probabilities for each bounding box, providing information about the type of object detected.
- **Loss Function**: It employs a combination of localization loss and classification loss during training to optimize predictions.

## Training YOLO Models
To train YOLO models for detecting washing machine timers and shafts, the following steps were followed:
- **Dataset Preparation**: Creation of a custom dataset containing images of washing machine timers and shafts with corresponding bounding box annotations.
- **Model Selection**: Utilization of the medium-sized YOLO model suitable for a wide range of object detection tasks.
- **Training Configuration**: Configuration of training parameters using the YOLO command-line tool with specified epochs, batch size, input image size, model type, and dataset configuration file.

## An example command used for training configuration:
```bash
yolo mode=train task=detect epochs=150 batch=8 imgz=640 model=yolov8m.pt data=custom.yaml
```
In this command:

🚀 mode=train: Specifies the training mode.

🔍 task=detect: Defines the detection task.

⏱️ epochs=150: Sets the number of training epochs to 150.

📦 batch=8: Specifies the batch size for training.

🖼️ imgz=640: Sets the input image size to 640x640 pixels.

🧠 model=yolov8m.pt: Specifies the YOLO model used for training.

📄 data=custom.yaml: Specifies the dataset configuration file.


## An example command used for Prediction:
```bash
yolo mode=predict task=detect conf=0.5 source=1.jpg show=True model=custom.pt
```

In this command:

🔮 mode=predict: Specifies prediction mode.

🔍 task=detect: Defines the detection task.

🎯 conf=0.5: Sets the confidence threshold for predictions to 0.5.

🖼️ source=1.jpg: Specifies the input image for prediction.

📺 show=True: Displays the predicted bounding boxes and associated class labels on the input image.

🧠 model=custom.pt: Specifies the trained YOLO model to use for predictions.

## Dataset 
The dataset provided encompasses a comprehensive collection of spare parts associated with washing machines, covering a wide spectrum of components essential for their functioning. It includes various categories such as timers, shafts, and an array of other integral parts crucial in the operation and maintenance of washing machines. This diverse dataset serves as a valuable resource for training and validating object detection models specifically tailored for identifying these essential components within the realm of washing machine systems.
 
[Data Set Link](https://drive.google.com/drive/folders/1T1E-4WB4jfuEpUaOrSF5Xxwroly-FDgY?usp=sharing)

## Demo
"E:\ICT 2020-2021\SEM 7\DL\Final Video Submit.mp4"
