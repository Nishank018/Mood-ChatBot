from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0
)

messages = [
    SystemMessage(content="You are a helpful AI assistant.")
]

print("-------------- Type 0 to exit the chat ---------------------")

while True:

    prompt = input("You: ")

    if prompt == "0":
        break

    messages.append(HumanMessage(content=prompt))

    response = llm.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)