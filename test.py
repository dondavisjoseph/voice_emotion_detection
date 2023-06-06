from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import speech_recognition as sr

def viewemotion():
    print("started...")
    # print(self.fpath)
    # path = self.fpath.get().strip()
    from scipy.io import wavfile
    path = wavfile.read('C:/Users/jeemo/Downloads/PROJECT/PROJECT/new.wav')

    print("path???", path)

    print(path)
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()
    print("khdgowdh")
    print(r)
    # Reading Audio file as source
    # listening the audio file and store in audio_text variable
    with sr.AudioFile(path) as source:
        audio_text = r.listen(source)
        print(audio_text)

        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
            paragraph = text

            lines_list = tokenize.sent_tokenize(paragraph)
            print(lines_list)

            NEG = NEU = POS = 0

            for sentence in lines_list:
                sid = SentimentIntensityAnalyzer()
                # print(sentence)

                ss = sid.polarity_scores(sentence)
                # print(ss)
                k = ss.keys()
                p = list(k)
                # print("P=",p)

                print("Negative:", ss.get(p[0]), ",Neutral:", ss.get(p[1]), ",Positive:", ss.get(p[2]), ",Sent:",
                      sentence)
                NEG = NEG + ss.get(p[0])
                NEU = NEU + ss.get(p[1])
                POS = POS + ss.get(p[2])
            if NEG > NEU:
                if NEG > POS:
                    print("Negative Emotion", NEG)
                else:
                    print("Positive Emotion", POS)
            else:
                if NEU > POS:
                    print("Neutral Emotion", NEU)
                else:
                    print("Positive Emotion", POS)

        except:
            print('Sorry.. run again...')
viewemotion()
