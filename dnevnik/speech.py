import speech_recognition as sr

r = sr.Recognizer()
def gruzia():
    with sr.Microphone() as source:
        print("Говорите...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        r_speech = r.recognize_google(audio, language='ru-RU')
        try:
            print("Вы сказали..." + r_speech)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))