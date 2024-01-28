from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings
import chatbot
import knowledge
import os

# init app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init vectorstore
knowledge.init()

# Mount the static directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

class ChatRequest(BaseModel):
    message: str

class UploadTextRequest(BaseModel):
    type: str  # 'global' or 'local'
    text: str # The text to be processed TODO: Change to file upload

class EnhanceTextRequest(BaseModel):
    type: str # 'global' or 'local'
    text: str # keywords on which to base text enhancement around
  
class ConvoTrigger(BaseModel):
    type: str # one of 6 metrics (not abstracted anywhere lol)
    threshold: int # threshold for metric to be triggered
    prompt: str # prompt to pass on to npc when triggered

class SetupDataModel(BaseModel):
    pass

class ConversationDataModel(BaseModel):
    pass

@app.post("/chat")
async def chat(chat_request: ChatRequest):
    #TODO: analyze request
    response = chatbot.get_response(chat_request.message)
    return {"response": response}
    #TODO: analyze response
    #TODO: stream response

@app.post("/add-trigger")
async def add_trigger(convo_trigger: ConvoTrigger):
    #TODO: add trigger to db (simple dict hosted here for now?)
    return {"status": "success"}

# Upload text to vector store memory
@app.post("/upload-text")
async def upload_text(upload_text_request: UploadTextRequest):
    knowledge.process_text(upload_text_request.type, upload_text_request.text)
    return {"status": "success"}

# Enhance vector store memory through generated text from keywords
# First check with user if the enhanced text is correct
@app.post("/enhance-text")
async def enhance_text(enhance_text_request: EnhanceTextRequest):
    res = knowledge.enhance_text(enhance_text_request.type, enhance_text_request.text)

# Setup metric-based events
@app.post("/setup-events")
async def setup_events(setup_data: SetupDataModel):
    # Process and store setup data
    return {"status": "success"}

# ?
@app.post("/analyze-conversation")
async def analyze_conversation(conversation_data: ConversationDataModel):
    # Real-time analysis logic
    return {"analysis": "Some analysis data"}
