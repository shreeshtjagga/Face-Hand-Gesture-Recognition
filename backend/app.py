from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import base64
import numpy as np
import joblib
import mediapipe as mp

app = Flask(__name__)
CORS(app)

# Load models and scalers
face_model = joblib.load('face_model.pkl')
face_scaler = joblib.load('face_model_scaler.pkl')
hand_model = joblib.load('hand_model.pkl')
hand_scaler = joblib.load('hand_model_scaler.pkl')

# Initialize MediaPipe
mp_face = mp.solutions.face_mesh.FaceMesh(static_image_mode=True)
mp_hand = mp.solutions.hands.Hands(static_image_mode=True, max_num_hands=1)

def extract_face_landmarks(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_face.process(rgb)
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        coords = []
        for lm in landmarks:
            coords.extend([lm.x, lm.y])
        return np.array(coords).reshape(1, -1)
    return None

def extract_hand_landmarks(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hand.process(rgb)
    if results.multi_hand_landmarks:
        landmarks = results.multi_hand_landmarks[0].landmark
        coords = []
        for lm in landmarks:
            coords.extend([lm.x, lm.y])
        return np.array(coords).reshape(1, -1)
    return None

@app.route('/detect', methods=['POST'])
def detect():
    try:
        data = request.get_json()
        img_data = data.get('image')

        # Decode base64 image
        img_bytes = base64.b64decode(img_data.split(',')[1])
        np_arr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Extract landmarks/features
        face_features = extract_face_landmarks(frame)
        hand_features = extract_hand_landmarks(frame)

        response = {}

        # Predict face emotion if detected
        if face_features is not None:
            face_scaled = face_scaler.transform(face_features)
            face_pred = face_model.predict(face_scaled)[0]
            response['face_emotion'] = face_pred
        else:
            response['face_emotion'] = 'No face detected'

        # Predict hand gesture if detected
        if hand_features is not None:
            hand_scaled = hand_scaler.transform(hand_features)
            hand_pred = hand_model.predict(hand_scaled)[0]
            response['hand_gesture'] = hand_pred
        else:
            response['hand_gesture'] = 'No hand detected'

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
