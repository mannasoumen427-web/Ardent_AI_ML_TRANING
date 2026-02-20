# 😊 Real-Time Emotion Detection using Deep Learning

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=for-the-badge&logo=keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Detect human emotions in real-time from a webcam feed using a custom-built CNN**

[![Portfolio](https://img.shields.io/badge/🌐%20Live%20Portfolio-Visit%20Now-7C4DFF?style=for-the-badge)](https://mannasoumen427-web.github.io/portfolio/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github)](https://github.com/mannasoumen427-web)

</div>

---

## 📌 Project Overview

This project implements a **real-time facial emotion recognition system** using:
- A custom **deep Convolutional Neural Network (CNN)** trained to classify 7 human emotions
- **OpenCV's Haar Cascade** classifier for fast face detection from a live webcam feed
- **Keras / TensorFlow** for model inference

The system captures video frames, detects faces, preprocesses them, and predicts the emotional state — all in real time.

---

## 🎯 Detected Emotions

The model classifies faces into **7 emotion categories**:

| # | Emotion | # | Emotion |
|---|---------|---|---------|
| 0 | 😡 Angry | 4 | 😢 Sad |
| 1 | 🤢 Disgust | 5 | 😲 Surprise |
| 2 | 😨 Fear | 6 | 😐 Neutral |
| 3 | 😄 Happy | | |

---

## 🧠 Model Architecture

The model is a **46-layer deep CNN** inspired by the Xception architecture, featuring **depthwise separable convolutions** and **residual (skip) connections** for efficient and accurate feature extraction.

```
Input: (64 × 64 × 1)  — Grayscale face image
  │
  ├─ Conv2D (8 filters, 3×3) + BatchNorm + ReLU          ← Entry Block
  ├─ Conv2D (8 filters, 3×3) + BatchNorm + ReLU
  │
  ├─ [Residual Block 1]                                   ← 16 filters
  │    SeparableConv2D × 2 + MaxPool(3×3) + Skip Conv2D
  │
  ├─ [Residual Block 2]                                   ← 32 filters
  │    SeparableConv2D × 2 + MaxPool(3×3) + Skip Conv2D
  │
  ├─ [Residual Block 3]                                   ← 64 filters
  │    SeparableConv2D × 2 + MaxPool(3×3) + Skip Conv2D
  │
  ├─ [Residual Block 4]                                   ← 128 filters
  │    SeparableConv2D × 2 + MaxPool(3×3) + Skip Conv2D
  │
  ├─ Conv2D (7 filters, 3×3)                              ← Classification Head
  ├─ GlobalAveragePooling2D
  └─ Softmax Activation → 7 Emotion Classes
```

### Key Design Choices

| Feature | Detail |
|---|---|
| **Input Shape** | `(64, 64, 1)` — Grayscale |
| **Total Layers** | 46 |
| **Convolution Type** | Depthwise Separable Conv2D (Xception-style) |
| **Skip Connections** | Residual `Add` layers at every block |
| **Regularization** | L2 weight decay (`0.01`) on all Conv layers |
| **Normalization** | BatchNormalization (`momentum=0.99`) throughout |
| **Pooling** | MaxPooling2D (`3×3`) + GlobalAveragePooling2D |
| **Output Activation** | Softmax (7 classes) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.8+** | Core language |
| **TensorFlow / Keras** | Model loading & inference |
| **OpenCV (cv2)** | Webcam capture & face detection |
| **NumPy** | Image preprocessing & array ops |
| **Haar Cascade XML** | Fast frontal face detection |
| **HDF5 (.hdf5)** | Trained model weights & config |

---

## 📁 Project Structure

```
emotion-detection/
├── emotion_detection.py                 # Main script — webcam inference pipeline
├── emotion_model.hdf5                   # Trained CNN model (weights + architecture)
├── haarcascade_frontalface_default.xml  # OpenCV face detector
└── README.md                            # Project documentation
```

---

## ⚙️ How It Works

```
┌─────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│  Webcam     │───▶│  Haar Cascade    │───▶│  Face ROI Extracted │
│  Frame      │    │  Face Detector   │    │  (cropped region)   │
└─────────────┘    └──────────────────┘    └────────┬────────────┘
                                                    │
                                           ┌────────▼────────────┐
                                           │  Preprocess         │
                                           │  Resize → 64×64     │
                                           │  Grayscale + Norm   │
                                           └────────┬────────────┘
                                                    │
                                           ┌────────▼────────────┐
                                           │  CNN Inference      │
                                           │  emotion_model.hdf5 │
                                           └────────┬────────────┘
                                                    │
                                           ┌────────▼────────────┐
                                           │  Predicted Emotion  │
                                           │  Displayed on Frame │
                                           └─────────────────────┘
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mannasoumen427-web/emotion-detection.git
cd emotion-detection
```

### 2. Install Dependencies

```bash
pip install tensorflow opencv-python numpy
```

### 3. Run the Detector

```bash
python emotion_detection.py
```

> **Note:** Make sure your webcam is connected. Press **`q`** to quit the live window.

---

## 📋 Requirements

```
tensorflow>=2.0
opencv-python>=4.5
numpy>=1.19
```

---

## 🔧 Configuration

You can adjust these parameters inside `emotion_detection.py`:

| Parameter | Default | Description |
|---|---|---|
| `MODEL_PATH` | `emotion_model.hdf5` | Path to trained model |
| `CASCADE_PATH` | `haarcascade_frontalface_default.xml` | Path to Haar cascade |
| `IMG_SIZE` | `64` | Input image size for the model |
| `scaleFactor` | `1.3` | Cascade scale factor for face detection |
| `minNeighbors` | `5` | Min neighbors for face detection confidence |

---

## 📊 Model Details Summary

| Property | Value |
|---|---|
| Architecture | Custom CNN (Xception-inspired) |
| Total Layers | 46 |
| Input | 64 × 64 grayscale |
| Output | 7-class Softmax |
| Format | Keras HDF5 (`.hdf5`) |
| Face Detector | Haar Cascade (OpenCV) |

---

## 🌱 Future Improvements

- [ ] Add training script with FER-2013 / AffectNet dataset
- [ ] Export model to ONNX / TFLite for edge deployment
- [ ] Build a Flask / FastAPI web interface
- [ ] Add confidence score display on video feed
- [ ] Support multi-face detection in a single frame
- [ ] Track emotion over time with a real-time graph

---

## 👤 Author

**Soumen Manna**
- 🌐 Portfolio: [mannasoumen427-web.github.io/portfolio](https://mannasoumen427-web.github.io/portfolio/)
- 💻 GitHub: [@mannasoumen427-web](https://github.com/mannasoumen427-web)

---


---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

<div align="center">

⭐ **If you found this project helpful, please give it a star!** ⭐

*Built with ❤️ | B.Sc CSE • Haldia Institute of Management*

</div>
