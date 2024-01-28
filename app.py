from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import chatbot
import knowledge
import analysis

# init app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "ws://localhost:8000/ws"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init vectorstore
knowledge.init()



# websocket endpoint
@app.websocket("/chat")
async def chat(websocket: WebSocket):
    await websocket.accept()

    while True:
        # frontend request (user prompt)
        prompt = await websocket.receive_text()

        # analyze prompt, return metrics and trigger events if necessary
        new_metrics, triggers = analysis.analyze_prompt(prompt)
        await websocket.send_json({"type": "analysis", "metrics": new_metrics, "triggers": triggers})

        # send npc response stream
        response = chatbot.get_response(prompt)
        for token in response:
            await websocket.send_json({"type": "response", "token": token})
        
        # await websocket.send_text(StreamingResponse(chatbot.stream_response(prompt)))

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

# class AnalysisResponse(BaseModel):
#     metrics: dict # metrics object
#     triggers: list # list of triggered events

class SetupDataModel(BaseModel):
    pass

class ConversationDataModel(BaseModel):
    pass



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
