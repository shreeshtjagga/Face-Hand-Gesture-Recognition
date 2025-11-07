 ## Facial Emotion and Hand Gesture Detection using MediaPipe & Machine Learning

##  Overview of my Project

This project presents a **real-time Facial Emotion and Hand Gesture Detection System** that leverages **MediaPipe** and **Machine Learning** to identify human facial expressions and hand gestures using a live webcam feed.  
The system aims to enhance **human–computer interaction** by enabling intuitive communication through **facial emotions** and **hand gestures**.

It can detect and classify multiple expressions such as *happy, sad, angry*, and recognize gestures like *thumbs up, peace, pointing,* and *open hand* in real-time.

---

##  Key Features

-  **Real-Time Detection:** Face and hand landmarks captured via webcam.  
-  **Emotion Recognition:** Detects happiness, sadness, and anger based on facial landmarks.  
-  **Gesture Recognition:** Recognizes common hand gestures like thumbs up, peace, etc.  
-  **Machine Learning Integration:** Uses a trained Random Forest model for classification.  
-  **Interactive GUI:** Displays live predictions for user engagement.  
-  **Model Serialization:** Models saved using Joblib for reusability.  

---

##  Tools & Technologies 

| Category | Tools Used |
|-----------|-------------|
| **Programming Languages** | Python, HTML, CSS, JavaScript |
| **Libraries & Frameworks** | MediaPipe, OpenCV, Scikit-learn, Joblib, Matplotlib |
| **Hardware Requirement** | Webcam-enabled device |
| **IDE / Environment** | VS Code, Jupyter Notebook, XAMPP (for web integration) |

---

##  Project Workflow

1. **Data Collection & Preprocessing**  
   - MediaPipe detects facial (468 points) and hand (21 points) landmarks.  
   - Extracted coordinates converted into numerical feature vectors.  

2. **Model Training**  
   - Random Forest Classifier trained on processed facial and gesture data.  
   - Models saved using Joblib (`.pkl` format).  

3. **Real-Time Detection**  
   - Live video feed analyzed using OpenCV.  
   - Facial expressions and gestures predicted and displayed on GUI.  

---

###  Clone the Repository

```bash
git clone https://github.com/<your-username>/Facial-Emotion-and-Hand-Gesture-Detection.git
cd Facial-Emotion-and-Hand-Gesture-Detection
