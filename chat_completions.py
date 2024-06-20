# https://platform.openai.com/docs/guides/text-generation/text-generation-models
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"
client = OpenAI()  # export OPENAI_API_KEY="sk-xxx" 已经set

# 多论对话
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },  # helps set the behavior of the assistant, optional
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  # 多论对话
        {"role": "user", "content": "Where was it played?"},
    ],
)

# assistant 开头也没问题
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  # 多论对话
        {"role": "user", "content": "Where was it played?"},
    ],
)

# 只有assistant 也没问题
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},  # 多论对话
    ],
)

pass
