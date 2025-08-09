import whisper
import cohere
import pyttsx3
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")



import cohere

co = cohere.Client(api_key)


co = cohere.Client(api_key)
model = whisper.load_model("base")


def speech_to_text(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]


def generate_response(prompt_text):
    response = co.generate(
        model='command',
        prompt=prompt_text,
        max_tokens=50,
        temperature=0.7,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.generations[0].text.strip()


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def main():
    audio_path = "input2.wav"
    print("جاري تحويل الصوت إلى نص...")
    user_text = speech_to_text(audio_path)
    print("النص المستخرج:", user_text)

    print("جاري توليد الرد من LLM...")
    reply = generate_response(user_text)
    print("الرد:", reply)

    print("جاري تحويل الرد إلى صوت وتشغيله...")
    text_to_speech(reply)


if __name__ == "__main__":
    main()
