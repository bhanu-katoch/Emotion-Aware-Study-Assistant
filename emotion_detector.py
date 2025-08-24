import os
import cv2
from deepface import DeepFace
from suggestion import get_suggestion
from collections import deque, Counter
import time

# Suppress TF warnings & fix threading issues
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

def detect_emotion():
    cap = cv2.VideoCapture(0)

    emotion_buffer = deque(maxlen=10)  # store last 10 detected emotions
    last_update = 0
    update_interval = 1  # seconds between suggestion updates
    current_suggestion = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # 1️⃣ Detect emotion
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

            # 3️⃣ Add to buffer
            emotion_buffer.append(emotion)

            # 4️⃣ Determine dominant emotion in buffer
            dominant_emotion = Counter(emotion_buffer).most_common(1)[0][0]

            # 5️⃣ Update suggestion every `update_interval` seconds
            if time.time() - last_update > update_interval:
                current_suggestion = get_suggestion(dominant_emotion)
                last_update = time.time()

            # 6️⃣ Display on webcam
            cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Suggestion: {current_suggestion}", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        except Exception as e:
            print("Error:", e)

        # Show webcam
        cv2.imshow("Emotion-Aware Study Assistant", frame)

        # Quit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_emotion()
