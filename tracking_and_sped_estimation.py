# -*- coding: utf-8 -*-
"""Tracking and Sped Estimation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EdsYMUwbSlQWhh0wd4nrjyfBr-zd9ok5
"""

import cv2
from ultralytics import YOLO

model = YOLO("/content/drive/MyDrive/best.pt")

video_path = ""

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
cap.release()

positions = {}

frame_idx = 0

for result in model.track(source=video_path, stream=True, tracker="bytetrack.yaml"):
    for box in result.boxes:
        track_id = box.id
        if track_id is None:
            continue
        x1, y1, x2, y2 = box.xyxy[0]
        centroid_x = (x1 + x2) / 2
        centroid_y = (y1 + y2) / 2
        if track_id not in positions:
            positions[track_id] = []
        positions[track_id].append((centroid_x, centroid_y, frame_idx))
        if len(positions[track_id]) >= 2:
            prev_pos = positions[track_id][-2]
            curr_pos = positions[track_id][-1]
            dx = curr_pos[0] - prev_pos[0]
            dy = curr_pos[1] - prev_pos[1]
            distance = (dx**2 + dy**2)**0.5
            frame_diff = curr_pos[2] - prev_pos[2]
            time_diff = frame_diff / fps
            if time_diff > 0:
                speed = distance / time_diff
                print(f"Frame {frame_idx}, Track {track_id}: speed = {speed:.2f} pixels/second")
    frame_idx += 1