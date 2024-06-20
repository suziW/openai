# https://platform.openai.com/docs/guides/embeddings/embeddings
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI()  # client.embeddings.create

response = client.embeddings.create(input="Your text string goes here", model="text-embedding-3-small")

print(response.data[0].embedding)
