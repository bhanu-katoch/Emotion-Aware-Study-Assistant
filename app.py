# app.py
import os
import cv2 
import streamlit as st 
from deepface import DeepFace 
from suggestion import get_suggestion
import numpy as np 

# ---------------- TensorFlow / DeepFace Fixes ----------------
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

st.title("Emotion-Aware Study Assistant 📚🙂")

# Info text
st.write("This app detects your emotion via webcam and provides study suggestions.")

# Create a placeholder for webcam feed
frame_placeholder = st.empty()

# Access webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        st.error("Cannot access webcam")
        break

    # Flip frame horizontally for mirror view
    frame = cv2.flip(frame, 1)

    try:
        # Detect emotion using DeepFace
        result = DeepFace.analyze(
            frame,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend="opencv"
        )

        if isinstance(result, list):
            emotion = result[0]['dominant_emotion']
        else:
            emotion = result['dominant_emotion']

        suggestion = get_suggestion(emotion)

        # Add text to frame
        cv2.putText(frame, f"Emotion: {emotion}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Suggestion: {suggestion}", (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    except Exception as e:
        st.warning(f"Error detecting emotion: {e}")

    # Convert frame (BGR to RGB) for Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")

    # Break loop if user closes Streamlit or presses stop
    if not cap.isOpened():
        break

cap.release()
