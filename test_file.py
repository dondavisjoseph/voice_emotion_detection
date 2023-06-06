# import speech_recognition as sr
#
# # Initialize recognizer
# r = sr.Recognizer()
#
# # Specify audio file path
# audio_path = "C:/Users/jeemo/Downloads/PROJECT/PROJECT/new.wav"
#
# # Load audio file
# with sr.AudioFile(audio_path) as source:
#     audio_text = r.record(source)   # Read the entire audio file
# print(audio_text)
# # Convert audio to text
# text = r.recognize_google(audio_text)
#
# # Print the converted text
# print("Converted text:")
# print(text)
import speech_recognition as sr
import nltk
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
# Initialize recognizer
r = sr.Recognizer()

# Specify audio file path
audio_path = "C:/Users/jeemo/Downloads/PROJECT/PROJECT/new.wav"

# Load audio file
with sr.AudioFile(audio_path) as source:
    audio_text = r.record(source)   # Read the entire audio file

# Convert audio to text
text = r.recognize_google(audio_text)

# Tokenize text into sentences
lines_list = sent_tokenize(text)

# Print the list of sentences
print("List of sentences:")
for line in lines_list:
    print(line)
