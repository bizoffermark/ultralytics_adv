from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="/home/aicenter/workspace/attack/phiat/phiat/configs/data/coco.yaml", epochs=100, imgsz=640)
