from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

client = Groq(api_key="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")

origins = [
    "http://127.0.0.1:5500",  
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    user_message: str

def get_groq_response(user_message: str) -> str:
    try:
        system_message = (
            "You are an AI assistant focused exclusively on the eLibrary domain. "
            "Your task is to provide accurate and relevant information related to books, "
            "including book suggestions, summaries, and providing book PDF download links. "
            "Do not engage in any other topics. Keep your responses concise, relevant, and strictly limited to eLibrary-related matters. "
            "If asked for a book, format the response like this: "
            "1. Title: The Great Gatsby Author: F. Scott Fitzgerald PDF Download: [Link](url) "
            "Always ensure the response is clean, structured, and focused on books only."
        )

        completion = client.chat.completions.create(
            model="mistral-saba-24b",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message},
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        # Extract and return the clean response
        if completion.choices:
            return completion.choices[0].message.content.strip()
        else:
            return "Sorry, I didn't get that."
        
    except Exception as e:
        return f"Error: {str(e)}"

@app.post("/send_message/")
async def send_message(message: Message):
    bot_response = get_groq_response(message.user_message)
    return {"bot_response": bot_response}
