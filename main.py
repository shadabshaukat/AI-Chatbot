from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import openai
import os

app = FastAPI()

# To serve the frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Use environment variable for OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('OPENAI_MODEL')

# Initialize a global conversation history
conversation_history = []

@app.post("/chat")
async def chat_with_openai(request: Request):
    global conversation_history
    try:
        data = await request.json()
        message = data.get('message')
        if not message:
            raise ValueError("No message provided")

        # Append the user's message to the conversation history
        conversation_history.append({"role": "user", "content": message})

        response = openai.ChatCompletion.create(
            model=model,
            messages=conversation_history
        )

        # Get the chatbot's response
        bot_message = response.choices[0].message['content']

        # Append the bot's response to the conversation history
        conversation_history.append({"role": "system", "content": bot_message})

        return {"response": bot_message}
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the detailed error
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload-documents/")
async def upload_documents(file: UploadFile = File(...)):
    # Process and store the file for RAG
    return {"filename": file.filename}

# Optional: Endpoint to clear the conversation history
@app.post("/reset-conversation")
async def reset_conversation():
    global conversation_history
    conversation_history = []
    return {"message": "Conversation history cleared."}
