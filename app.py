from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import chatbot
import knowledge

app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

class ChatRequest(BaseModel):
    message: str

class UploadTextRequest(BaseModel):
    type: str  # 'global' or 'local'
    text: str

class SetupDataModel(BaseModel):
    pass

class ConversationDataModel(BaseModel):
    pass

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    response = chatbot.get_response(chat_request.message)
    return {"response": response}

@app.post("/upload-text")
async def upload_text(upload_text_request: UploadTextRequest):
    knowledge.process_text(upload_text_request.type, upload_text_request.text)
    return {"status": "success"}

@app.post("/enhance-text")
async def enhance_text(enhance_text_request: EnhanceTextRequest):
    res = knowledge.enhance_text(enhance_text_request.type, enhance_text_request.text)

@app.post("/setup-events")
async def setup_events(setup_data: SetupDataModel):
    # Process and store setup data
    return {"status": "success"}

@app.post("/analyze-conversation")
async def analyze_conversation(conversation_data: ConversationDataModel):
    # Real-time analysis logic
    return {"analysis": "Some analysis data"}
