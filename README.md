# 📖 Emotion-Aware Study Assistant  

An **ML-based mini project** that detects student emotions in real-time using facial recognition and provides **adaptive study suggestions** based on mood.  

---

## 🚀 Features  
- 🎭 Detects emotions (happy, sad, neutral, angry, fear, surprise, disgust) from webcam.  
- 📚 Suggests adaptive study actions based on mood.  
- 🖥️ Works as a simple webcam demo (OpenCV) or a web app (Streamlit).  
- ⚡ Built using pre-trained **DeepFace** models for quick setup.  

---

## 🛠️ Tech Stack  
- **Python** (ML + Backend)  
- **OpenCV** – real-time webcam capture  
- **DeepFace** – pre-trained emotion recognition  
- **TensorFlow/Keras** – underlying ML framework  
- **Streamlit** – optional web-based interface  

---

## 📂 Project Structure  
```sh
Emotion-Aware-Study-Assistant/
│── app.py # Streamlit web app
│── emotion_detector.py # Webcam-based emotion detection
│── suggestion.py # Maps emotion → study suggestion
│── requirements.txt # Dependencies
│── README.md # Project description & usage
```

---

## ⚙️ Installation & Setup  

1️⃣ Clone the project (or copy into a folder):  
```bash
git clone https://github.com/bhanu-katoch/Emotion-Aware-Study-Assistant.git
cd Emotion-Aware-Study-Assistant

2️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```

3️⃣ Run webcam demo:
```sh
python emotion_detector.py
```

4️⃣ Run web app (Streamlit):
```sh
streamlit run app.py
```
## 🎯 How It Works

```sh
[ Webcam Feed ] 
       │
       ▼
[ Emotion Detection (DeepFace) ]
       │
       ▼
[ Emotion → Suggestion Mapping ]
       │
       ▼
[ Display to Student (Webcam / Web App) ]
```
📊 Example

- Emotion Detected: Sad 😔

- Suggestion: "Take a short break ☕, then revise easy concepts."

## 📌 Future Enhancements

- 🔊 Add voice-based emotion detection.

- 📝 Integrate text sentiment analysis (student journal input).

- 📱 Mobile-friendly app for students.

- 🤖 Multi-modal system (face + voice + text).

## 🏆 Learning Outcomes

- Applied machine learning in real-time applications.

- Learned to integrate computer vision + education technology.

- Built a mini-project prototype for emotion-aware study assistance.