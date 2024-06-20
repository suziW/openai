# https://platform.openai.com/docs/guides/text-to-speech/text-to-speech
from pathlib import Path
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI()  # client.audio.speech.create

for voice in ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]:  # 只有6个voice，后2个是女声
    speech_file_path = "./speech_{}.mp3".format(voice)

    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input="嗨，大家好!",
    )
    response.write_to_file(speech_file_path)
