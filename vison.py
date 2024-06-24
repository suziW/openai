# https://platform.openai.com/docs/guides/vision/vision
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI()  # client.chat.completions.create

"""
While it does understand the relationship between objects in images, 
it is not yet optimized to answer detailed questions about the location of certain objects in an image
"""
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "这个图片里面有什么?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://content-management-files.canva.com/cdn-cgi/image/f=auto,q=70/da85060c-9286-4245-b0eb-fd98d1907cf2/magic-photo_promo-showcase_012x.png",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])

"""
{
  "id": "chatcmpl-9dI66w2wdiEnEUi9In5MxnOOhI6CX",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "这张图片展示了一个熊猫骑着自行车在城市中行驶的场景。旁边的界面是Canva的一个创意工具，左侧面板显示为 \"Magic Media\"，提供了图片、图形和视频选项。面板中还有不同的风格选择和纵横比选择，其中一张图片是黄色鸭子的插画风格。",
        "role": "assistant"
      }
    }
  ],
  "created": 1719151386,
  "model": "gpt-4o-2024-05-13",
  "object": "chat.completion",
  "system_fingerprint": "fp_9cb5d38cf7",
  "usage": {
    "completion_tokens": 83,
    "prompt_tokens": 777,
    "total_tokens": 860
  }
}
"""