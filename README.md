# 🚗 Vehicle Object Detection & Speed Estimation 📈

> **Internship Project**  
> **Jan 2024 – Jun 2024**

---

## 🔍 Overview
This repository contains an end-to-end pipeline for **real-time vehicle detection** and **speed calculation** using YOLOv8 and BYTETrack. The model was first trained on an 8K self-annotated dataset (Roboflow), fine-tuned on UAV imagery, and integrated into a live tracking module to compute vehicle speeds from video feeds.

---

## 🛠️ Key Components
1. **Data Annotation** ✍️  
   - Annotated ~2,000 satellite/UAV images in Roboflow  
   - Classes: `car`, `truck`, `bus`  
2. **Model Training** 🤖  
   - Base detector: **YOLOv8**  
   - Training schedule: 300 epochs, batch size 16  
   - Fine-tuned on UAV dataset for high-altitude accuracy  
3. **Multi-Object Tracking** 🚀  
   - Integrated **BYTETrack** for frame-to-frame identity preservation  
4. **Speed Estimation** 🏎️  
   - Pixel-to-meter conversion using known camera FOV  
   - Distance measured between two reference lines  
   - Time stamped via frame rate (FPS)  
   - Speed = distance (m) / time (s), output in km/h  
