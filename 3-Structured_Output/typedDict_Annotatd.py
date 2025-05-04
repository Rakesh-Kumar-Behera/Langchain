from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

#schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["Pos","neg"], "return sentiment of the review as positive, negative or neutral"]
    pros: Annotated[Optional[list[str]], "List of pros mentioned in the review"]
    cons: Annotated[Optional[list[str]], "List of cons mentioned in the review"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Excellent Phone. Value for Money.
Performance: The phone performs efficiently in most tasks, handling apps and multitasking with ease.
Design: The design is sleek and modern, offering a premium look and feel. The build quality is solid.
Speed: The speed is impressive, particularly while launching apps and navigating the interface.
Charging: The charging speed is excellent, allowing for quick power-ups, which is highly convenient for busy schedules.
Battery: The battery life is reliable and lasts a full day with moderate to heavy use.""")

print(result)
# print(result.summary)
# print(result.sentiment)
# print(result.pros)
# print(result.cons)


# """Camera Performance:

# The Pixel 9's camera has consistently impressed me, particularly in low-light environments. The AI-driven image processing is exceptional, capturing intricate details and vibrant colors. While I have occasionally observed slight overexposure or blown-out highlights in bright lighting conditions, these are minor issues that don't significantly detract from the overall quality. I believe a software update could potentially address these inconsistencies.

# Battery Life:

# While the Pixel 9's battery generally meets my needs, there have been instances where it hasn't quite lived up to my expectations. I've also noticed minimal battery drain in ideal conditions, such as when the phone is idle with minimal activity. The Always-On Display feature, which provides clear and readable visuals even in low-light conditions, has not had a substantial impact on my daily battery life.

# Software:

# The Pixel's Material interface is both visually pleasing and user-friendly. For those transitioning from iOS, the Pixel's customization options offer a refreshing change.

# Build Quality:

# The Pixel 9 is a well-crafted device with a premium build quality that surpasses that of the iPhone 15 series.

# Chipset and Performance:

# The Pixel 9's performance is adequate for everyday tasks. While I don't rely heavily on mobile gaming or demanding applications, I've found the chipset to handle my daily needs effectively. The addition of an ultrasonic fingerprint sensor is a welcome feature that addresses a long-standing desire of Pixel users."""