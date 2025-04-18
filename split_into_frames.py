import cv2
import os

video_path = "./videos/challenge_color_848x480.mp4"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

video = cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration = int(frame_count / fps)

print(f"Video FPS: {fps}, Total frames: {frame_count}, Duration: {duration} seconds")

frame_number = 0
for sec in range(duration):
    frame_number = int(sec * fps)
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, frame = video.read()
    if success:
        filename = os.path.join(output_folder, f"frame_{sec:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
    else:
        print(f"Failed at second {sec}")

video.release()
