# app.py
import streamlit as st
import cv2
from deepface import DeepFace
from suggestion import get_suggestion

st.title("Emotion-Aware Study Assistant")

run = st.checkbox("Start Camera")
camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret:
        break
    
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        st.image(frame, channels="BGR")
        st.write(f"Detected Emotion: **{emotion}**")
        st.write(f"Study Suggestion: {get_suggestion(emotion)}")
    except:
        st.write("No face detected. Try again.")
