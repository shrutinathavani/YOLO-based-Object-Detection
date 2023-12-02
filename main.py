#used for training:

yolo mode=train task=detect model=yolov8l.pt epochs=100 data=config.yaml 

#used for testing
yolo mode=predict task=detect model=best.pt conf=0.8 show=True source=1.jpg