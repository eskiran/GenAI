from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

import os

load_dotenv()
project = os.getenv("GOOGLE_CLOUD_PROJECT")


llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    vertexai = True,
    project = project
)

country = input("please enter the country of your choice? ")
messages = [
    SystemMessage("you are social teacher of primary school, explain interestic facts also"),
    HumanMessage(f"what is capital of {country} ? ")
]

response = llm.invoke(messages)
print(response.content)