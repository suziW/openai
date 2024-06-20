# https://platform.openai.com/docs/guides/text-generation/text-generation-models
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"
client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     response_format={"type": "json_object"}, # enable JSON mode
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant designed to output JSON."}, # 还要指定一下json
#         {"role": "user", "content": "Who won the world series in 2020?"},
#     ],
# )
# print(response.choices[0].message.content) # 输出达到最大限制可能不全，也不保证 matche any specific schema

# # 缺失指定json, 会报错, 不在prompt 说要json的话，模型可能输出不正常
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     response_format={"type": "json_object"}, # enable JSON mode
#     messages=[
#         {"role": "user", "content": "Who won the world series in 2020?"},
#     ],
# )
# print(response.choices[0].message.content) # 输出达到最大限制可能不全，也不保证 matche any specific schema


# 试试不指定json mode, 确实不太行
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."}, # 还要指定一下json
        {"role": "user", "content": "Who won the world series in 2020?"},
    ],
)
print(response.choices[0].message.content) # 输出达到最大限制可能不全，也不保证 matche any specific schema
