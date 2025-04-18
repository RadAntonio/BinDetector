from ultralytics import YOLO
import cv2
import os

model_path = "./runs/detect/train2/weights/best.pt"
input_folder = "frames"
output_folder = "annotated_frames2"

os.makedirs(output_folder, exist_ok=True)

model = YOLO(model_path)

detection_array = []

if os.path.exists(output_folder):
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)

            results = model.predict(input_path, conf=0.49)

            has_detections = len(results[0].boxes) > 0
            detection_array.append(1 if has_detections else 0)

            annotated_image = results[0].plot()
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, annotated_image)

print(f"All frames saved: '{output_folder}'")
print("Detection array:", detection_array)
