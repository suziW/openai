# https://platform.openai.com/docs/guides/speech-to-text/speech-to-text
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI()  # client.audio.transcriptions

audio_file = open("./hello.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
)
print(transcription.text)

transcription = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

print(transcription)