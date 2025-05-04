from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

#schema
json_schema = {
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["Pos", "neg"],
      "description": "Return sentiment of the review as positive, negative or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "List of pros mentioned in the review"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "List of cons mentioned in the review"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the Reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""Excellent Phone. Value for Money.
Performance: The phone performs efficiently in most tasks, handling apps and multitasking with ease.
Design: The design is sleek and modern, offering a premium look and feel. The build quality is solid.
Speed: The speed is impressive, particularly while launching apps and navigating the interface.
Charging: The charging speed is excellent, allowing for quick power-ups, which is highly convenient for busy schedules.
Battery: The battery life is reliable and lasts a full day with moderate to heavy use.
Reviews by Marnus Petersen""")

print(result)
print(result['name'])


