from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.yaml") # build a new model from scratch

result = model.train(data="config.yaml", epochs=100) # train the model

