# Facial Emotion and Hand Gesture Detection

A real-time system that detects **facial emotions** and **hand gestures** from live webcam input using **MediaPipe** and **Machine Learning**.  
The project focuses on improving **human–computer interaction** through intuitive visual recognition.

---

## Project Overview

The application captures live video using a webcam, extracts facial and hand landmarks with MediaPipe, and applies a trained **Random Forest** model to classify emotions and gestures in real time.

**Facial Emotions:** Happy, Sad, Angry  
**Hand Gestures:** Thumbs Up, Peace, Pointing, Open Hand

---

## Key Features
- Real-time facial and hand landmark detection
- Facial emotion recognition using machine learning
- Hand gesture recognition from live webcam feed
- Random Forest–based classification
- Live prediction display through a simple web-based GUI

---

## Tech Stack
- Python
- MediaPipe, OpenCV
- Scikit-learn (Random Forest), Joblib
- HTML, CSS, JavaScript

---

## How It Works
MediaPipe extracts landmark coordinates from the webcam feed.  
These landmarks are converted into feature vectors and classified using a trained Random Forest model to predict emotions and gestures in real time.

---

## How to Run

```bash
git clone https://github.com/shreeshtjagga/Facial-Emotion-and-Hand-Gesture-Detection.git
cd Facial-Emotion-and-Hand-Gesture-Detection

# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend (open new terminal)
cd frontend
python -m http.server 8000

# Open application in web(local host)
http://localhost:8000
