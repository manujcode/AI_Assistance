import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

print("perfect!!")
load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY



def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: ", text)
        return text
    except sr.UnknownValueError:
        print("sorry, could not understand the audio")
    except sr.RequestError as e:
        print("could not request result from google speech recognition service: {0}".format(e))
    

def text_to_speech(text):
    tts=gTTS(text=text, lang="en")
    
    #save the speech from the given text in the mp3 format
    tts.save("speech.mp3")

def llm_model_object(user_text):
    # Configure the API with your key
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Use the updated model name format
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")
    
    # Generate content safely
    try:
        response = model.generate_content(user_text)
        result = response.text
        return result
    except Exception as e:
        print(f"Error generating content: {e}")
        return f"Sorry, I encountered an error: {str(e)}"
    