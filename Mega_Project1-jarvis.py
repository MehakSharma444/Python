import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "9a573bd0f40040eb8e14411b11972c05"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="")
    completion = client.chat.completions.create(
    model ="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content":"You are a vitual assistant named jarvis skilled i general tasks like Alexa and Google Cloud"},
        {"role":"user","content":command}])
    return completion.choices[0].message.content
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open insta" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "play" in c.lower():
        s = c.lower().split(" ")
        for song in s:
            if song in musicLibrary.music.keys():
                link = musicLibrary.music[song]
                webbrowser.open(link)
                break
    elif "news" in c.lower():
        url = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Check if the request was successful
        if url.status_code == 200:
            print("📰 Top News Headlines (US):\n")
            data = url.json()
            articles = data.get('articles',[])
            for article in articles:
                print(article['title'])
                speak(article['title'])
    elif "stop" in c.lower() or "exit" in c.lower():
        speak("Shutting down. Goodbye!")
        exit()

    else:
        output = aiProcess(c)
        speak(output)
if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1.5)
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print("you said :" ,word)
            if(word.lower() == "jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1.5)
                    speak("Jarvis Activate...")
                    print("Jarvis Activated.... ")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                print("you said :", command)
                processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
        except Exception as e:
            print("Error;{0}".format(e))
