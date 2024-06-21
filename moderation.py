# https://platform.openai.com/docs/guides/moderation/moderation
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI()  # client.moderations.create

response = client.moderations.create(input="狗日的，来草我逼逼，mua~")

output = response.results[0]

"""'
Our support for non-English languages is currently limited:
中文表现不行

{
  "id": "modr-9cPKBF2JvXPGeEnJfBICYvCsPhI1Q",
  "model": "text-moderation-007",
  "results": [
    {
      "categories": {
        "harassment": false,
        "harassment/threatening": false,
        "hate": false,
        "hate/threatening": false,
        "self-harm": false,
        "self-harm/instructions": false,
        "self-harm/intent": false,
        "sexual": false,
        "sexual/minors": false,
        "violence": false,
        "violence/graphic": false,
        "self-harm": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": false
      },
      "category_scores": {
        "harassment": 0.03374599665403366,
        "harassment/threatening": 0.0008903731359168887,
        "hate": 0.000728921964764595,
        "hate/threatening": 4.595153768605087e-7,
        "self-harm": 0.00006452447996707633,
        "self-harm/instructions": 4.5360999934018764e-7,
        "self-harm/intent": 0.000014790502973482944,
        "sexual": 0.00470712361857295,
        "sexual/minors": 0.0006423030863516033,
        "violence": 0.006989033427089453,
        "violence/graphic": 0.000017982763893087395,
        "self-harm": 0.00006452447996707633,
        "sexual/minors": 0.0006423030863516033,
        "hate/threatening": 4.595153768605087e-7,
        "violence/graphic": 0.000017982763893087395,
        "self-harm/intent": 0.000014790502973482944,
        "self-harm/instructions": 4.5360999934018764e-7,
        "harassment/threatening": 0.0008903731359168887
      },
      "flagged": false
    }
  ]
}
"""
