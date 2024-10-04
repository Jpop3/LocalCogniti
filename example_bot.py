from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#You are an Academic Advisor, specializing in mathematics, at the University of Sydney. 
#The user is a Year 12 student who needs advice on what mathematic pathways to take for a given degree and their mathematical background.

template = """ 
You are an expert at the video game Rocket League!

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

model = OllamaLLM(model = "llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to Chatbot")
    while True:
        user_input = input("You : ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()