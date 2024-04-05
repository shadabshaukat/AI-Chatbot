from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import openai
import os

app = FastAPI()

# Add this before running Uvicorn to print all routes
for route in app.routes:
    methods = ','.join(route.methods)
    print(f"Path: {route.path}, Methods: {methods}")

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

@app.post("/chat")
async def chat_with_openai(request: Request):
    try:
        data = await request.json()
        message = data.get('message')
        if not message:
            raise ValueError("No message provided")

        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": message}]
        )
        return {"response": response.choices[0].message['content']}
    except Exception as e:
        print(f"Error occurred: {e}")  # Log the detailed error
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload-documents/")
async def upload_documents(file: UploadFile = File(...)):
    # Process and store the file for RAG
    return {"filename": file.filename}
