def get_suggestion(emotion):
    suggestions = {
        "happy": "Great mood! Try solving challenging problems 🎯",
        "neutral": "Stay steady! Revise or practice light topics 📘",
        "sad": "Take a short break ☕, then revise easy concepts",
        "angry": "Cool down with a small break 🧘, avoid heavy topics",
        "fear": "Relax! Start with confidence-building exercises 💡",
        "surprise": "Channel the energy into brainstorming ideas ✨",
        "disgust": "Pause & reset! Do something fun for 5 minutes 🎶"
    }
    return suggestions.get(emotion, "Keep learning at your own pace!")
