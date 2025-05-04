from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

#schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I was initially hesitant to purchase the S25 Ultra, but after 2 weeks of use, I'm thrilled to share my overwhelmingly positive experience!

The battery life has been a standout feature for me, consistently lasting a full day and often stretching into the next with moderate to heavy use.

The phone's overall performance has been seamless, with lightning-fast app loading, effortless multitasking, and silky-smooth graphics.

The display is stunning, with vibrant colors and crisp details that make every visual experience a joy.

I've also been impressed with the camera's capabilities, delivering crisp, high-quality photos and videos in a variety of conditions.

Overall, the S25 Ultra has exceeded my expectations and truly lives up to its reputation as an Android powerhouse. If you're in the market for a new flagship device, I highly recommend giving this one a serious look!""")

print(result)
print(result['summary'])
print(result['sentiment'])