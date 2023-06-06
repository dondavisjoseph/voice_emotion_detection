# voice_emotion_detection

Project Summary

Voice-Based Emotion Detection and YouTube Link Recommendation

This project aims to develop a graphical user interface (GUI) application for voice-based emotion detection and YouTube link recommendation. The application allows users to record their voice, analyzes the recorded audio to detect emotions, and suggests relevant YouTube links based on the detected emotions.

Key Features:
1. Voice Recording: Users can specify the duration of voice recordings and capture their voice using the system's microphone.
2. Emotion Detection: The recorded voice is transcribed using the Google Speech Recognition API, and sentiment analysis is performed using the SentimentIntensityAnalyzer from the NLTK library. The sentiment scores are used to determine the dominant emotion expressed in the voice (negative, neutral, or positive).
3. YouTube Link Recommendation: Based on the detected emotion, the application recommends YouTube links that align with the expressed emotion. The links are opened in a web browser for the user to view related content.
4. Graphical User Interface: The application provides a user-friendly GUI using the tkinter library, allowing users to interact with the system easily.
5. Exception Handling: The code includes appropriate exception handling to handle potential errors during voice recording, file selection, and speech recognition.

