# https://platform.openai.com/docs/guides/images/image-generation
from openai import OpenAI
import os

os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI()  # client.images.generate

response = client.images.generate(
    model="dall-e-3",
    prompt="a dog like tiger: diger",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url


"""
dalle-e-2 response:
{
  "created": 1718933222,
  "data": [
    {
      "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-GPF3I0oh4Wlii472bjaAphP2/user-Vadpe9QaGD7y9rUJUJVyauPh/img-5cf8V0VLSt50mRSmLtCJnbQP.png?st=2024-06-21T00%3A27%3A02Z&se=2024-06-21T02%3A27%3A02Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-20T23%3A34%3A27Z&ske=2024-06-21T23%3A34%3A27Z&sks=b&skv=2023-11-03&sig=dFDtDw8zlSApMRbAHYGqmye98XdqQWHrP1tCACkXHQ0%3D"
    }
  ]
}
"""

"""
dalle-e-2 response: 会生成一个 revised_prompt
{
  "created": 1718940277,
  "data": [
    {
      "revised_prompt": "Visualize a fascinating hybrid animal that combines features of a dog and a tiger. The creature known as a 'Diger' should have the loyalty and friendly demeanor of a dog with the bold stripes and formidable presence of a tiger. This unique creation will exhibit charisma of its canine lineage and the strength and majesty of its feline lineage. It stands proudly against a natural backdrop of dense jungle foliage, its tail wagging amiably while its eyes reflect the predatory instinct of a tiger.",
      "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-GPF3I0oh4Wlii472bjaAphP2/user-Vadpe9QaGD7y9rUJUJVyauPh/img-E4HsDfZQE3mP8sca2Q94BsVg.png?st=2024-06-21T02%3A24%3A37Z&se=2024-06-21T04%3A24%3A37Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-20T23%3A38%3A31Z&ske=2024-06-21T23%3A38%3A31Z&sks=b&skv=2023-11-03&sig=gIZF6ie3ZBmuuwWbN%2Bpd5Rpjf1W%2B4NvkTqMhsUvzLZs%3D"
    }
  ]
}
"""
