import os
import cv2
from deepface import DeepFace
from suggestion import get_suggestion

# Suppress TF warnings & fix threading issues
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

def detect_emotion():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break   # stop if no frame

        try:
            # 1️⃣ Detect emotion using DeepFace (force OpenCV backend for stability)
            result = DeepFace.analyze(
                frame, 
                actions=['emotion'], 
                enforce_detection=False,
                detector_backend="opencv"
            )

            # 2️⃣ Handle dict vs list output
            if isinstance(result, list):
                emotion = result[0]['dominant_emotion']
            else:
                emotion = result['dominant_emotion']

            # 3️⃣ Get study suggestion
            suggestion = get_suggestion(emotion)

            # 4️⃣ Show text on webcam feed
            cv2.putText(frame, f"Emotion: {emotion}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.putText(frame, f"Suggestion: {suggestion}", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        except Exception as e:
            print("Error:", e)   # helpful debugging

        # Show webcam
        cv2.imshow("Emotion-Aware Study Assistant", frame)

        # Quit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_emotion()
